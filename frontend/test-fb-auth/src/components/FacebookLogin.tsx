import { useEffect } from "react";

const FacebookLogin = () => {
  const apiBaseUrl = import.meta.env.VITE_API_BASE_URL;

  const handleFacebookLogin = () => {
    window.location.href = `${apiBaseUrl}/facebook/auth/login`;
  };

  useEffect(() => {
    // CATCH CALLBACK

    // GET THE 'code' in the query params of the URL
    const params = new URLSearchParams(window.location.search);
    const code = params.get("code");

    // Call /callback
    // get user info in this route!
    if (code) {
      fetch(`${apiBaseUrl}/facebook/auth/callback?code=${code}`)
        .then((res) => res.json())
        .then((data) => {
          console.log("User Info:", data);
        })
        .catch((err) => console.error("Error during Facebook OAuth:", err));
    }
  }, []);

  //TODO: Store token to storage

  return (
    <div>
      <h1>Sign in with FB Below!</h1>
      <button onClick={handleFacebookLogin}>Login with Facebook</button>
    </div>
  );
};

export default FacebookLogin;
