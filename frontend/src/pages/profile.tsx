import React from 'react';
import Layout from '@theme/Layout';
import ProfileDisplay from '../components/ProfileDisplay';
import ProfileEdit from '../components/ProfileEdit';
import clsx from 'clsx';

export default function ProfilePage() {
    return (
        <Layout title="Personalization Profile" description="Manage your AI-Native learning preferences">
            <main className="container margin-vert--xl">
                <div className="row">
                    <div className="col col--8 col--offset-2">
                        <div className="text--center margin-bottom--xl">
                            <h1 style={{ 
                                fontSize: '3rem', 
                                background: 'linear-gradient(135deg, #00D9FF 0%, #7C3AED 100%)',
                                WebkitBackgroundClip: 'text',
                                WebkitTextFillColor: 'transparent'
                            }}>
                                User Intelligence Profile
                            </h1>
                            <p style={{ fontSize: '1.2rem', color: 'rgba(255,255,255,0.7)' }}>
                                Personalize your AI Tutor's responses and learning experience
                            </p>
                        </div>
                        
                        <div className="row">
                            <div className="col col--6">
                                <ProfileDisplay />
                            </div>
                            <div className="col col--6">
                                <ProfileEdit />
                            </div>
                        </div>
                    </div>
                </div>
            </main>
        </Layout>
    );
}