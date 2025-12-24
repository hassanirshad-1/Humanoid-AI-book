import React, { useEffect, useState } from 'react';
import api from '../services/api';
import clsx from 'clsx';

export default function ProfileDisplay() {
    const [profile, setProfile] = useState<any>(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState<string | null>(null);

    useEffect(() => {
        const fetchProfile = async () => {
            try {
                const response = await api.get('/users/me');
                setProfile(response.data);
            } catch (err) {
                console.error('Failed to fetch profile', err);
                setError('Authentication required to view profile.');
            } finally {
                setLoading(false);
            }
        };

        fetchProfile();
    }, []);

    if (loading) {
        return (
            <div className="card shadow--md" style={{ background: 'rgba(255,255,255,0.05)', border: '1px solid rgba(0,217,255,0.2)' }}>
                <div className="card__body text--center">
                    <div className="loading-spinner"></div>
                    <p>Scanning neural profile...</p>
                </div>
            </div>
        );
    }

    if (error) {
        return (
            <div className="alert alert--warning" role="alert">
                {error}
            </div>
        );
    }

    return (
        <div className="card shadow--md" style={{ 
            height: '100%',
            background: 'rgba(255,255,255,0.05)', 
            border: '1px solid rgba(0,217,255,0.2)',
            backdropFilter: 'blur(10px)'
        }}>
            <div className="card__header">
                <h3 style={{ color: 'var(--ifm-color-primary)' }}>Neural Status</h3>
            </div>
            <div className="card__body">
                <div className="margin-bottom--md">
                    <label style={{ fontSize: '0.8rem', textTransform: 'uppercase', opacity: 0.6 }}>Identity</label>
                    <div style={{ fontSize: '1.1rem', fontWeight: 'bold' }}>{profile.name}</div>
                    <div style={{ fontSize: '0.9rem', opacity: 0.8 }}>{profile.email}</div>
                </div>
                
                <div className="margin-bottom--md">
                    <label style={{ fontSize: '0.8rem', textTransform: 'uppercase', opacity: 0.6 }}>Cognitive Level</label>
                    <div className="badge badge--primary" style={{ display: 'block', padding: '0.5rem', marginTop: '0.2rem' }}>
                        {profile.skill_level || 'Not Configured'}
                    </div>
                </div>

                <div className="margin-bottom--md">
                    <label style={{ fontSize: '0.8rem', textTransform: 'uppercase', opacity: 0.6 }}>Operational System</label>
                    <div className="badge badge--secondary" style={{ display: 'block', padding: '0.5rem', marginTop: '0.2rem' }}>
                        {profile.operating_system || 'Not Configured'}
                    </div>
                </div>
            </div>
        </div>
    );
}