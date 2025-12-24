import express from "express";
import cors from "cors";
import morgan from "morgan";
import { toNodeHandler } from "better-auth/node";
import { auth } from "./auth";

const app = express();

// Logging
app.use(morgan("dev"));

// Body parsing
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Enable CORS for the frontend
app.use(cors({
    origin: process.env.FRONTEND_URL || "http://localhost:3000",
    credentials: true
}));

// Better-Auth handler
app.all("/api/auth/*path", toNodeHandler(auth));

const PORT = process.env.PORT || 3001; // Using 3001 to avoid conflict with Docusaurus if it runs on 3000
app.listen(PORT, () => {
    console.log(`Better-Auth server running on http://localhost:${PORT}`);
});
