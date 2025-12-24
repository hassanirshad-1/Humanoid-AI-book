import React, { useState, useEffect } from 'react';
import Layout from '@theme/Layout';
import { useAuth } from '../context/AuthContext';
import api from '../services/api';
import Link from '@docusaurus/Link';
import { useHistory } from '@docusaurus/router';
import useBaseUrl from '@docusaurus/useBaseUrl';
import clsx from 'clsx';
import styles from './index.module.css'; 

export default function RegisterPage() {
    const [name, setName] = useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [skillLevel, setSkillLevel] = useState('Beginner');
    const [operatingSystem, setOperatingSystem] = useState('Windows');
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState('');
    
    const { login } = useAuth();
    const history = useHistory();
    const homePath = useBaseUrl('/');

    // Password strength calculation
    const calculateStrength = (pwd: string) => {
        let score = 0;
        if (!pwd) return { score: 0, text: '', color: '' };
        
        if (pwd.length >= 8) score += 1;
        if (pwd.length >= 12) score += 1;
        if (/[A-Z]/.test(pwd)) score += 1;
        if (/[0-9]/.test(pwd)) score += 1;
        if (/[^A-Za-z0-9]/.test(pwd)) score += 1;

        let text = 'Weak';
        let color = '#ff4d4f'; // red

        if (score >= 3) {
            text = 'Medium';
            color = '#faad14'; // orange
        }
        if (score >= 5) {
            text = 'Strong';
            color = '#52c41a'; // green
        }

        return { score, text, color };
    };

    const { score: strength, text: strengthText, color: strengthColor } = calculateStrength(password);

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        setLoading(true);
        setError('');

        try {
            // Register on Python backend
            await api.post('/auth/register', { 
                email, 
                password, 
                name,
                skill_level: skillLevel,
                operating_system: operatingSystem
            });

            // Automatically log in after registration
            const formData = new URLSearchParams();
            formData.append('username', email);
            formData.append('password', password);
            
            const loginRes = await api.post('/auth/jwt/login', formData, {
                headers: { 'Content-Type': 'application/x-www-form-urlencoded' }
            });

            if (loginRes.data.access_token) {
                login(loginRes.data.access_token);
                history.push(homePath);
            }
        } catch (err: any) {
            console.error('Registration failed', err);
            if (err.response?.data?.detail === 'REGISTER_USER_ALREADY_EXISTS') {
                setError('This email is already registered. Please login.');
            } else if (err.response?.data?.detail) {
                 setError(`Registration failed: ${err.response.data.detail}`);
            } else {
                setError('Registration failed. Please try again.');
            }
        } finally {
            setLoading(false);
        }
    };

    return (
        <Layout title="Register" description="Create your account to access personalized AI tutoring">
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
                                <h1 style={{ color: 'var(--ifm-color-primary)' }}>Create Account</h1>
                                <p>Join the AI-Native Robotics Learning Platform</p>
                            </div>
                            <div className="card__body">
                                {error && (
                                    <div className="alert alert--danger margin-bottom--md" role="alert">
                                        {error}
                                    </div>
                                )}
                                <form onSubmit={handleSubmit}>
                                    <div className="margin-bottom--md">
                                        <label className="header-label" htmlFor="name">Full Name</label>
                                        <input 
                                            id="name"
                                            className="button button--block button--outline button--secondary"
                                            style={{ textAlign: 'left', cursor: 'text', background: 'rgba(0,0,0,0.2)', color: 'white' }}
                                            type="text" 
                                            placeholder="Enter your name"
                                            value={name} 
                                            onChange={(e) => setName(e.target.value)} 
                                            required 
                                        />
                                    </div>

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

                                    <div className="margin-bottom--md">
                                        <label className="header-label" htmlFor="password">Password</label>
                                        <input 
                                            id="password"
                                            className="button button--block button--outline button--secondary"
                                            style={{ textAlign: 'left', cursor: 'text', background: 'rgba(0,0,0,0.2)', color: 'white', marginBottom: '0.5rem' }}
                                            type="password" 
                                            placeholder="••••••••"
                                            value={password} 
                                            onChange={(e) => setPassword(e.target.value)} 
                                            required 
                                        />
                                        
                                        {/* Password Strength Indicator */}
                                        {password && (
                                            <div style={{ padding: '0 0.5rem' }}>
                                                <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '0.2rem', fontSize: '0.8rem' }}>
                                                    <span>Strength:</span>
                                                    <span style={{ color: strengthColor, fontWeight: 'bold' }}>{strengthText}</span>
                                                </div>
                                                <div style={{ height: '4px', width: '100%', background: 'rgba(255,255,255,0.1)', borderRadius: '2px' }}>
                                                    <div style={{ 
                                                        height: '100%', 
                                                        width: `${Math.min(strength * 20, 100)}%`, 
                                                        background: strengthColor, 
                                                        borderRadius: '2px',
                                                        transition: 'all 0.3s ease'
                                                    }} />
                                                </div>
                                            </div>
                                        )}
                                    </div>

                                    <div className="margin-bottom--md">
                                        <label className="header-label" htmlFor="skillLevel">Robotics Skill Level</label>
                                        <select 
                                            id="skillLevel"
                                            className="button button--block button--outline button--secondary"
                                            style={{ textAlign: 'left', cursor: 'pointer', background: 'rgba(0,0,0,0.2)', color: 'white' }}
                                            value={skillLevel}
                                            onChange={(e) => setSkillLevel(e.target.value)}
                                        >
                                            <option value="Beginner" style={{color: 'black'}}>Beginner (I'm new to robotics)</option>
                                            <option value="Intermediate" style={{color: 'black'}}>Intermediate (I know some concepts)</option>
                                            <option value="Advanced" style={{color: 'black'}}>Advanced (I build robots)</option>
                                        </select>
                                    </div>

                                    <div className="margin-bottom--lg">
                                        <label className="header-label" htmlFor="operatingSystem">Primary Operating System</label>
                                        <select 
                                            id="operatingSystem"
                                            className="button button--block button--outline button--secondary"
                                            style={{ textAlign: 'left', cursor: 'pointer', background: 'rgba(0,0,0,0.2)', color: 'white' }}
                                            value={operatingSystem}
                                            onChange={(e) => setOperatingSystem(e.target.value)}
                                        >
                                            <option value="Windows" style={{color: 'black'}}>Windows</option>
                                            <option value="macOS" style={{color: 'black'}}>macOS</option>
                                            <option value="Linux" style={{color: 'black'}}>Linux</option>
                                        </select>
                                    </div>

                                    <button 
                                        type="submit" 
                                        className="button button--primary button--block"
                                        disabled={loading}
                                        style={{ fontSize: '1.1rem', fontWeight: 'bold' }}
                                    >
                                        {loading ? 'Creating Account...' : 'Register'}
                                    </button>
                                </form>
                            </div>
                            <div className="card__footer text--center">
                                <p>
                                    Already have an account? <Link to="/login">Login here</Link>
                                </p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </Layout>
    );
}
