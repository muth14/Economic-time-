import React from 'react';
import Sidebar from '@/components/layout/Sidebar';
import Header from '@/components/layout/Header';
import { WorkspaceProvider } from '@/context/WorkspaceContext';
import '@/styles/globals.css';

export const metadata = {
  title: 'INDUSTRIAL BRAIN - Enterprise Industrial AI Operating System',
  description: 'The Unified Asset & Operations Intelligence Platform powered by Knowledge Graphs, Vector Search, and Multi-Agent Swarms.',
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en" className="dark">
      <body className="bg-background text-slate-100 flex min-h-screen antialiased">
        <WorkspaceProvider>
          <Sidebar />
          <div className="flex-1 flex flex-col min-w-0">
            <Header />
            <main className="flex-1 p-6 overflow-y-auto">
              {children}
            </main>
          </div>
        </WorkspaceProvider>
      </body>
    </html>
  );
}
