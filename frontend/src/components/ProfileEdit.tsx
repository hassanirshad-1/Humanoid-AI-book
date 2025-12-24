import React, { useState, useEffect } from 'react';
import api from '../services/api';
import clsx from 'clsx';

export default function ProfileEdit() {
    const [skillLevel, setSkillLevel] = useState('');
    const [os, setOs] = useState('');
    const [saving, setSaving] = useState(false);
    const [message, setMessage] = useState<{ text: string, type: 'success' | 'error' } | null>(null);

    useEffect(() => {
        const fetchCurrent = async () => {
            try {
                const response = await api.get('/users/me');
                setSkillLevel(response.data.skill_level || 'Beginner');
                setOs(response.data.operating_system || 'Windows');
            } catch (err) {
                console.error('Failed to fetch profile', err);
            }
        };
        fetchCurrent();
    }, []);

    const handleSave = async (e: React.FormEvent) => {
        e.preventDefault();
        setSaving(true);
        setMessage(null);
        try {
            await api.patch('/users/me', {
                skill_level: skillLevel,
                operating_system: os
            });
            setMessage({ text: 'Neural profile synchronized!', type: 'success' });
            // Refresh page to update display component
            setTimeout(() => window.location.reload(), 1500);
        } catch (err) {
            console.error('Update failed', err);
            setMessage({ text: 'Synchronization failed. Check uplink.', type: 'error' });
        } finally {
            setSaving(false);
        }
    };

    return (
        <div className="card shadow--md" style={{ 
            height: '100%',
            background: 'rgba(255,255,255,0.05)', 
            border: '1px solid rgba(124, 58, 237, 0.3)',
            backdropFilter: 'blur(10px)'
        }}>
            <div className="card__header">
                <h3 style={{ color: 'var(--accent-purple)' }}>Reconfigure Profile</h3>
            </div>
            <div className="card__body">
                <form onSubmit={handleSave}>
                    <div className="margin-bottom--md">
                        <label className="header-label">Update Skill Level</label>
                        <select 
                            value={skillLevel} 
                            onChange={(e) => setSkillLevel(e.target.value)}
                            className="button button--block button--outline button--secondary"
                            style={{ textAlign: 'left', background: 'rgba(0,0,0,0.2)', color: 'white' }}
                        >
                            <option value="Beginner" style={{color: 'black'}}>Beginner</option>
                            <option value="Intermediate" style={{color: 'black'}}>Intermediate</option>
                            <option value="Advanced" style={{color: 'black'}}>Advanced</option>
                        </select>
                    </div>
                    <div className="margin-bottom--lg">
                        <label className="header-label">Update Operating System</label>
                        <select 
                            value={os} 
                            onChange={(e) => setOs(e.target.value)}
                            className="button button--block button--outline button--secondary"
                            style={{ textAlign: 'left', background: 'rgba(0,0,0,0.2)', color: 'white' }}
                        >
                            <option value="Windows" style={{color: 'black'}}>Windows</option>
                            <option value="macOS" style={{color: 'black'}}>macOS</option>
                            <option value="Linux" style={{color: 'black'}}>Linux</option>
                        </select>
                    </div>
                    <button 
                        type="submit" 
                        disabled={saving}
                        className="button button--primary button--block"
                        style={{ fontWeight: 'bold' }}
                    >
                        {saving ? 'Synchronizing...' : 'Apply Changes'}
                    </button>
                </form>
                {message && (
                    <div className={clsx('alert margin-top--md', {
                        'alert--success': message.type === 'success',
                        'alert--danger': message.type === 'error'
                    })} role="alert">
                        {message.text}
                    </div>
                )}
            </div>
        </div>
    );
}