import { SvelteKitAuth } from '@auth/sveltekit';
import GitHub from '@auth/core/providers/github';
import GoogleProvider from '@auth/core/providers/google';
import { AUTH_SECRET, AUTH_GITHUB_CLIENT_ID, AUTH_GITHUB_CLIENT_SECRET, AUTH_GOOGLE_CLIENT_ID, AUTH_GOOGLE_CLIENT_SECRET } from '$env/static/private';

export const handle = SvelteKitAuth({
	secret: AUTH_SECRET,
	providers: [
		GitHub({ clientId: AUTH_GITHUB_CLIENT_ID, clientSecret: AUTH_GITHUB_CLIENT_SECRET }),
		GoogleProvider({ clientId: AUTH_GOOGLE_CLIENT_ID, clientSecret: AUTH_GOOGLE_CLIENT_SECRET }),
	],
});