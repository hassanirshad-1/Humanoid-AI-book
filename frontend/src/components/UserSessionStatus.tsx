import React from 'react';
import { useAuth } from '../context/AuthContext';
import Link from '@docusaurus/Link';
import useBaseUrl from '@docusaurus/useBaseUrl';

export default function UserSessionStatus() {
    const { user, isAuthenticated, isLoading, logout } = useAuth();
    const homeUrl = useBaseUrl('/');

    // Helper to get initials
    const getInitials = (name: string) => {
        if (!name) return '??';
        return name
            .split(' ')
            .map(n => n[0])
            .slice(0, 2)
            .join('')
            .toUpperCase();
    };

    if (isLoading) {
        return <div style={{ width: '32px', height: '32px' }} />;
    }

    if (!isAuthenticated) {
        return (
            <div className="navbar__item" style={{ display: 'flex', gap: '0.5rem', alignItems: 'center' }}>
                <Link to="/login" className="button button--secondary button--sm">Login</Link>
                <Link to="/register" className="button button--primary button--sm">Register</Link>
            </div>
        );
    }

    const initials = getInitials(user?.name || user?.email || 'User');

    return (
        <div className="navbar__item dropdown dropdown--hoverable dropdown--right">
            <div 
                className="navbar__link" 
                style={{ 
                    display: 'flex', 
                    alignItems: 'center', 
                    padding: '0 8px',
                    cursor: 'pointer'
                }}
            >
                <div style={{
                    width: '36px',
                    height: '36px',
                    borderRadius: '50%',
                    background: 'linear-gradient(135deg, #00D9FF, #7C3AED)',
                    color: 'white',
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'center',
                    fontWeight: 'bold',
                    fontSize: '14px',
                    border: '2px solid rgba(255, 255, 255, 0.2)',
                    boxShadow: '0 0 10px rgba(0, 217, 255, 0.3)'
                }}>
                    {initials}
                </div>
            </div>
            <ul className="dropdown__menu">
                <li>
                    <div className="dropdown__header">
                        <span style={{ fontWeight: 'bold', display: 'block' }}>{user?.name}</span>
                        <span style={{ fontSize: '0.8rem', opacity: 0.7 }}>{user?.email}</span>
                    </div>
                </li>
                <li className="dropdown__divider" />
                <li>
                    <Link className="dropdown__link" to="/profile">
                        Neural Profile
                    </Link>
                </li>
                <li>
                    <Link 
                        className="dropdown__link" 
                        to="#" 
                        onClick={(e) => {
                            e.preventDefault();
                            logout();
                        }}
                    >
                        Disconnect
                    </Link>
                </li>
            </ul>
        </div>
    );
}
