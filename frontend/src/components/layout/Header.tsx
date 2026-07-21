'use client';

import React, { useState } from 'react';
import { Search, ChevronRight, Activity } from 'lucide-react';

export default function Header() {
  const [searchQuery, setSearchQuery] = useState('');

  return (
    <header className="h-14 bg-white/95 backdrop-blur-md border-b border-stone-200 px-6 flex items-center justify-between sticky top-0 z-30 font-sans">
      {/* Left Breadcrumbs & Project Switcher */}
      <div className="flex items-center gap-3 text-xs font-medium text-stone-600">
        <span className="font-bold text-stone-900 font-mono tracking-wide">INDUSTRIAL BRAIN</span>
        <ChevronRight className="w-3.5 h-3.5 text-stone-400" />
        <span className="bg-stone-100 px-2.5 py-1 rounded text-stone-700 font-mono text-[11px] border border-stone-200 font-bold">
          GenChem Refinery Production
        </span>
      </div>

      {/* Right Actions & System Status */}
      <div className="flex items-center gap-3">
        {/* Global Search Bar */}
        <div className="relative w-60 md:w-80">
          <Search className="w-3.5 h-3.5 absolute left-3 top-1/2 -translate-y-1/2 text-stone-400" />
          <input
            type="text"
            placeholder="Search equipment tag, document, or asset..."
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            className="w-full bg-stone-50 border border-stone-200 rounded-lg pl-8 pr-3 py-1.5 text-xs text-stone-900 placeholder-stone-400 focus:outline-none focus:border-blue-600 font-mono transition-all"
          />
        </div>

        {/* System Active Status Badge */}
        <div className="px-3 py-1.5 rounded-lg bg-emerald-50 border border-emerald-200 text-emerald-700 text-xs font-mono font-bold flex items-center gap-2">
          <span className="w-2 h-2 rounded-full bg-emerald-500 animate-pulse" />
          <span>AI Gateway Ready</span>
        </div>

        {/* User Profile Avatar */}
        <div className="flex items-center gap-2 pl-2 border-l border-stone-200">
          <div className="w-7 h-7 rounded-full bg-slate-900 text-white font-extrabold text-xs flex items-center justify-center font-mono shadow-xs">
            M
          </div>
        </div>
      </div>
    </header>
  );
}

