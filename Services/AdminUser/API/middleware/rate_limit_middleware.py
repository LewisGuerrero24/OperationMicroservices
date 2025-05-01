import time
from collections import defaultdict
from django.http import JsonResponse, HttpResponse

class RateLimitMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.requests = defaultdict(list) # {ip: [timestamps]}
        self.rate = 10 # máximo 10 solicitudes
        self.period = 60 # en 60 segundos
        self.block_time = 120  # bloquear IP por 120 segundos si se pasa
        self.blocked_ips = {} 

    def __call__(self, request):
        ip = self.get_ip(request)
        now = time.time()

        # revisamos si la IP está bloqueada
        if ip in self.blocked_ips:
            block_end = self.blocked_ips[ip]
            if now < block_end:
                return HttpResponse('Rate limit exceeded', status=429)
            else:
                del self.blocked_ips[ip] # desbloqueamos IP
        
        # Limpiar solicitudes viejas
        self.requests[ip] = [timestamp for timestamp in self.requests[ip] if now - timestamp < self.period]

        # Registrar esta solicitud
        self.requests[ip].append(now)

        # Revisar si se pasó del límite
        if len(self.requests[ip]) > self.rate:
            self.blocked_ips[ip] = now + self.block_time
            return JsonResponse({'detail': 'Rate limit exceeded. You are temporarily blocked.'}, status=429)

        response = self.get_response(request)
        return response

    
    def get_ip(self, request):
        """Obtener IP real (incluso detrás de proxy)."""
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip