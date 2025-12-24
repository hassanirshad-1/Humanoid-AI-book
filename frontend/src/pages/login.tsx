import React, { useState } from 'react';
import Layout from '@theme/Layout';
import { useAuth } from '../context/AuthContext';
import api from '../services/api';
import Link from '@docusaurus/Link';
import { useHistory } from '@docusaurus/router';
import useBaseUrl from '@docusaurus/useBaseUrl';
import clsx from 'clsx';
import styles from './index.module.css';

export default function LoginPage() {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState('');

    const { login } = useAuth();
    const history = useHistory();
    const homePath = useBaseUrl('/');

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        setLoading(true);
        setError('');

        try {
            // FastAPI Users JWT login expects x-www-form-urlencoded
            const formData = new URLSearchParams();
            formData.append('username', email);
            formData.append('password', password);

            const response = await api.post('/auth/jwt/login', formData, {
                headers: { 'Content-Type': 'application/x-www-form-urlencoded' }
            });

            if (response.data.access_token) {
                login(response.data.access_token);
                history.push(homePath);
            }
        } catch (err: any) {
            console.error('Login failed', err);
            // Enhanced error logging
            if (err.response && err.response.data) {
                console.error('Backend error data:', err.response.data);
                const detail = err.response.data.detail;
                if (detail) {
                    // specific fastapi-users errors
                    if (detail === "LOGIN_BAD_CREDENTIALS") {
                        setError("Invalid email or password.");
                    } else if (typeof detail === 'string') {
                        setError(`Login failed: ${detail}`);
                    } else {
                        setError("Login failed. Check console for details.");
                    }
                } else {
                    setError('Login failed. Please check your credentials.');
                }
            } else {
                setError('Login failed. Network or server error.');
            }
        } finally {
            setLoading(false);
        }
    };

    return (
        <Layout title="Login" description="Login to your AI-Native Robotics Learning Platform account">
            <div className="container margin-vert--xl">
                <div className="row">
                    <div className="col col--6 col--offset-3">
                        <div className={clsx('card', styles.authCard)} style={{
                            backdropFilter: 'blur(10px)',
                            backgroundColor: 'rgba(255, 255, 255, 0.05)',
                            border: '1px solid rgba(0, 217, 255, 0.2)',
                            boxShadow: '0 0 20px rgba(0, 217, 255, 0.1)'
                        }}>
                            <div className="card__header text--center">
                                <h1 style={{ color: 'var(--ifm-color-primary)' }}>Welcome Back</h1>
                                <p>Login to continue your robotics journey</p>
                            </div>
                            <div className="card__body">
                                {error && (
                                    <div className="alert alert--danger margin-bottom--md" role="alert">
                                        {error}
                                    </div>
                                )}
                                <form onSubmit={handleSubmit}>
                                    <div className="margin-bottom--md">
                                        <label className="header-label" htmlFor="email">Email Address</label>
                                        <input
                                            id="email"
                                            className="button button--block button--outline button--secondary"
                                            style={{ textAlign: 'left', cursor: 'text', background: 'rgba(0,0,0,0.2)', color: 'white' }}
                                            type="email"
                                            placeholder="name@example.com"
                                            value={email}
                                            onChange={(e) => setEmail(e.target.value)}
                                            required
                                        />
                                    </div>

                                    <div className="margin-bottom--lg">
                                        <label className="header-label" htmlFor="password">Password</label>
                                        <input
                                            id="password"
                                            className="button button--block button--outline button--secondary"
                                            style={{ textAlign: 'left', cursor: 'text', background: 'rgba(0,0,0,0.2)', color: 'white' }}
                                            type="password"
                                            placeholder="••••••••"
                                            value={password}
                                            onChange={(e) => setPassword(e.target.value)}
                                            required
                                        />
                                    </div>

                                    <button
                                        type="submit"
                                        className="button button--primary button--block"
                                        disabled={loading}
                                        style={{ fontSize: '1.1rem', fontWeight: 'bold' }}
                                    >
                                        {loading ? 'Logging In...' : 'Login'}
                                    </button>
                                </form>
                            </div>
                            <div className="card__footer text--center">
                                <p>
                                    Don't have an account? <Link to="/register">Create one here</Link>
                                </p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </Layout>
    );
}