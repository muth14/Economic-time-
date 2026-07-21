'use client';

import React from 'react';
import Link from 'next/link';
import { usePathname } from 'next/navigation';
import { 
  Layers, 
  FileText, 
  Network, 
  Boxes, 
  Bot, 
  BarChart3, 
  Sparkles, 
  Cpu, 
  Activity
} from 'lucide-react';

const navSections = [
  {
    title: 'GET STARTED',
    items: [
      { href: '/', label: '1. Workspace', icon: Layers }
    ]
  },
  {
    title: 'INTELLIGENCE BUILD',
    items: [
      { href: '/documents', label: '2. Documents', icon: FileText },
      { href: '/graph', label: '3. Knowledge Graph', icon: Network },
      { href: '/digital-twin', label: '4. Equipment DNA', icon: Boxes }
    ]
  },
  {
    title: 'LIVE REASONING',
    items: [
      { href: '/copilot', label: '5. Evidence Copilot', icon: Bot },
      { href: '/analytics', label: '6. Executive Dashboard', icon: BarChart3 },
      { href: '/innovations', label: '7. Innovation Hub', icon: Sparkles }
    ]
  }
];

export default function Sidebar() {
  const pathname = usePathname();

  return (
    <aside className="w-64 bg-white border-r border-stone-200 min-h-screen flex flex-col justify-between p-4 z-40 relative">
      <div>
        {/* Brand Header */}
        <div className="flex items-center gap-2.5 px-3 py-3 mb-6 border-b border-stone-100">
          <div className="w-8 h-8 rounded-lg bg-gradient-to-br from-blue-600 to-indigo-700 flex items-center justify-center shadow-md">
            <Cpu className="w-5 h-5 text-white" />
          </div>
          <div>
            <h1 className="font-extrabold text-sm text-stone-900 tracking-tight flex items-center gap-1 font-sans">
              INDUSTRIAL <span className="text-[10px] bg-blue-50 text-blue-700 border border-blue-200 px-1.5 py-0.5 rounded font-mono font-bold">BRAIN</span>
            </h1>
            <p className="text-[10px] text-stone-500 font-mono">Enterprise AI Platform</p>
          </div>
        </div>

        {/* Grouped Nav Items */}
        <div className="space-y-6">
          {navSections.map((section) => (
            <div key={section.title} className="space-y-1">
              <h3 className="px-3 text-[10px] font-bold font-mono text-stone-400 uppercase tracking-wider mb-2">
                {section.title}
              </h3>
              {section.items.map((item) => {
                const Icon = item.icon;
                const isActive = pathname === item.href;

                return (
                  <Link
                    key={item.href}
                    href={item.href}
                    className={`flex items-center gap-2.5 px-3 py-2 rounded-lg text-xs font-semibold font-sans transition-all duration-150 ${
                      isActive
                        ? 'bg-blue-50 text-blue-700 border border-blue-200 shadow-xs'
                        : 'text-stone-600 hover:text-stone-900 hover:bg-stone-100/80'
                    }`}
                  >
                    <Icon className={`w-4 h-4 ${isActive ? 'text-blue-600' : 'text-stone-400'}`} />
                    <span>{item.label}</span>
                  </Link>
                );
              })}
            </div>
          ))}
        </div>
      </div>

      {/* Footer System Status */}
      <div className="mt-8 pt-4 border-t border-stone-200 px-2">
        <div className="bg-stone-50 border border-stone-200 p-3 rounded-xl flex items-center justify-between">
          <div className="flex items-center gap-2">
            <span className="w-2 h-2 rounded-full bg-emerald-500 animate-pulse" />
            <span className="text-xs text-stone-700 font-mono font-medium">AI Swarm Engine</span>
          </div>
          <span className="text-[10px] bg-emerald-100 text-emerald-800 px-2 py-0.5 rounded font-mono font-bold">Active</span>
        </div>
      </div>
    </aside>
  );
}

