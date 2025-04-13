export const APP_PORT = process.env.APP_PORT ? parseInt(process.env.APP_PORT, 10) : 3000;
export const APP_IS_PROD = process.env.NODE_ENV === 'prod';
