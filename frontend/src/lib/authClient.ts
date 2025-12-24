/**
 * frontend/src/lib/authClient.ts
 * 
 * Better-Auth client configuration.
 */

import { createAuthClient } from "better-auth/react";

const getBaseURL = () => {
    if (typeof process !== 'undefined' && process.env.REACT_APP_BETTER_AUTH_BASE_URL) {
        return process.env.REACT_APP_BETTER_AUTH_BASE_URL;
    }
    return "http://localhost:3001/api/auth";
};

export const authClient = createAuthClient({
    // URL of the Node.js Better-Auth service
    baseURL: getBaseURL(),
    fetchOptions: {
        onSuccess: (ctx) => {
            // Capture the session token and store it for the Python API axios instance
            // Better-Auth might return the token in the headers or the body depending on config
            const authToken = ctx.response.headers.get("set-auth-token") || (ctx.data as any)?.token;
            if (authToken) {
                console.log("Successfully captured auth token");
                localStorage.setItem("bearer_token", authToken);
            } else {
                console.warn("Auth success but no token captured in headers or body");
            }
        }
    }
});

export const { useSession, signIn, signOut, signUp } = authClient;
