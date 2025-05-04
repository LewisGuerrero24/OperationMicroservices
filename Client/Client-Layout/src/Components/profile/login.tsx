function Login() {
    return (
      <section className="hero is-fullheight has-background-link">
        <div className="hero-body">
          <div className="container">
            <div className="columns is-centered">
              <div className="column is-4">
                <div className="card">
                  <div className="card-content">
                    <div className="content has-text-primary">
                        <h1 >Login</h1>
                    </div>
                    <div className="field">
                      <p className="control has-icons-left has-icons-right">
                        <input className="input" type="email" placeholder="Email" />
                        <span className="icon is-small is-left">
                          <i className="fas fa-envelope"></i>
                        </span>
                        <span className="icon is-small is-right">
                          <i className="fas fa-check"></i>
                        </span>
                      </p>
                    </div>
                    <div className="field">
                      <p className="control has-icons-left">
                        <input className="input" type="password" placeholder="Password" />
                        <span className="icon is-small is-left">
                          <i className="fas fa-lock"></i>
                        </span>
                      </p>
                    </div>
                    <div className="field">
                      <p className="control">
                        <button className="button is-success is-fullwidth">
                          Login
                        </button>
                      </p>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
    );
  }
  
  export default Login;
  