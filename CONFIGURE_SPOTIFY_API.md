# ⚙ Spotify API configuration
This section provides a step-by-step guide on how to set up a Spotify application, enabling `Spotify Linker` to access data on the currently playing music.

## ✨ Create Spotify Application 
1. Log in to the [Spotify Developer Dashboard](https://developer.spotify.com/documentation/web-api).
2. Once logged in, navigate to your profile and select `Dashboard`.
3. On the `Dashboard` click on "Create app".
4. Fill in all the required fields, as illustrated below. The configuration details are generally straightforward, with the exception of the "Redirect URI," which should point to localhost.

![spotify_create_app](https://github.com/ImFireGod/SteelSeries-Spotify-Linker/assets/49344172/baea1ae9-6144-4862-a5e2-a10cef855c9d)

5. Go to the `Settings` page of the newly created application.
6. Copy both your `Spotify Client ID` and `Spotify Client Secret` from this page.

![spotify_app_dashboard](https://github.com/ImFireGod/SteelSeries-Spotify-Linker/assets/49344172/e3ee8d60-12f2-49f8-a268-9f32b726b1f5)


7. Configuration  

Copy and paste the following information into the `config.json` file or follow the installation prompt from `install.bat`.  

```JS
{
    "spotify_client_id": "SPOTIFY_CLIENT_ID",
    "spotify_client_secret": "YOUR_SPOTIFY_CLIENT_SECRET",
    "spotify_redirect_uri": "http://localhost:2408/callback",
    "local_port": 2408,
    ...
}
```
> ⚠️ Local port must match with the spotify redirect uri