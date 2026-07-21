'use client';

import React from 'react';
import { 
  ShieldCheck, 
  AlertTriangle, 
  FileText, 
  CheckCircle2, 
  Download,
  Zap
} from 'lucide-react';

export default function CompliancePage() {
  return (
    <div className="space-y-6 max-w-7xl mx-auto">
      {/* Header */}
      <div className="flex items-center justify-between border-b border-slate-800 pb-4">
        <div>
          <h1 className="text-2xl font-extrabold text-white flex items-center gap-2">
            <ShieldCheck className="w-6 h-6 text-emerald-400" /> Compliance Intelligence & Audit Assistant
          </h1>
          <p className="text-xs text-slate-400 mt-0.5">
            ISO 55001, OISD-137, PESO, Factory Act Violation Detector & Autonomous Audit Evidence Package
          </p>
        </div>

        <button className="px-4 py-2 bg-gradient-to-r from-emerald-500 to-teal-600 text-white font-semibold text-xs rounded-xl flex items-center gap-2 shadow-lg hover:opacity-90 transition-all">
          <Download className="w-4 h-4" /> Download Complete Audit Package (.ZIP)
        </button>
      </div>

      {/* Main Grid */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        {/* Compliance Scores */}
        <div className="glass-panel p-5 rounded-2xl border border-slate-700/60 space-y-4">
          <h2 className="text-sm font-bold text-white uppercase tracking-wider font-mono">Standard Compliance Scores</h2>

          <div className="space-y-3">
            <div className="p-3 bg-slate-900 rounded-xl border border-slate-800 space-y-1">
              <div className="flex justify-between text-xs font-mono">
                <span className="text-slate-300 font-bold">ISO 55001 Asset Management</span>
                <span className="text-emerald-400 font-bold">92.0%</span>
              </div>
              <div className="w-full h-1.5 bg-slate-800 rounded-full overflow-hidden">
                <div className="h-full bg-emerald-500 rounded-full" style={{ width: '92%' }} />
              </div>
            </div>

            <div className="p-3 bg-slate-900 rounded-xl border border-slate-800 space-y-1">
              <div className="flex justify-between text-xs font-mono">
                <span className="text-slate-300 font-bold">OISD-137 Fire & Safety</span>
                <span className="text-amber-400 font-bold">81.5%</span>
              </div>
              <div className="w-full h-1.5 bg-slate-800 rounded-full overflow-hidden">
                <div className="h-full bg-amber-500 rounded-full" style={{ width: '81.5%' }} />
              </div>
            </div>

            <div className="p-3 bg-slate-900 rounded-xl border border-slate-800 space-y-1">
              <div className="flex justify-between text-xs font-mono">
                <span className="text-slate-300 font-bold">PESO Pressure Vessel Regs</span>
                <span className="text-emerald-400 font-bold">89.0%</span>
              </div>
              <div className="w-full h-1.5 bg-slate-800 rounded-full overflow-hidden">
                <div className="h-full bg-emerald-500 rounded-full" style={{ width: '89%' }} />
              </div>
            </div>
          </div>
        </div>

        {/* Violations & Evidence Package */}
        <div className="lg:col-span-2 glass-panel p-6 rounded-2xl border border-slate-700/60 space-y-5">
          <h2 className="text-base font-bold text-white flex items-center gap-2">
            <AlertTriangle className="w-4 h-4 text-amber-400" /> Active Compliance Violations (2 Flagged)
          </h2>

          <div className="space-y-3">
            <div className="p-4 rounded-xl bg-amber-950/30 border border-amber-500/40 space-y-1.5">
              <div className="flex items-center justify-between text-xs font-mono font-bold">
                <span className="text-amber-400">OISD-137 Section 6.2 (High Severity)</span>
                <span className="text-slate-400">Affected: Pump P-101</span>
              </div>
              <p className="text-xs text-slate-200">
                Emergency isolation valve response time delayed by 1.4 seconds beyond safety threshold.
              </p>
              <p className="text-[11px] text-amber-300 font-mono">Remediation: Replace solenoid pilot valve and test closure speed.</p>
            </div>

            <div className="p-4 rounded-xl bg-slate-900 border border-slate-800 space-y-1.5">
              <div className="flex items-center justify-between text-xs font-mono font-bold">
                <span className="text-cyan-400">PESO Pressure Vessel Reg 14 (Medium)</span>
                <span className="text-slate-400">Affected: Tank T-301</span>
              </div>
              <p className="text-xs text-slate-200">
                Feedwater Tank T-301 safety relief valve re-certification due in 14 days.
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
