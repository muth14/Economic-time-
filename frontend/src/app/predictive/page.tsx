'use client';

import React from 'react';
import { 
  Activity, 
  Flame, 
  Calendar, 
  AlertTriangle, 
  ShieldAlert, 
  ArrowRight,
  TrendingDown
} from 'lucide-react';

const assetHealthList = [
  { id: "V-101", name: "Steam Control Valve V-101", rul_days: 6, fail_prob: 0.78, risk: "Red", health: 42.0, next_maint: "2026-07-26" },
  { id: "P-101", name: "Boiler Feed Pump P-101", rul_days: 18, fail_prob: 0.35, risk: "Orange", health: 64.5, next_maint: "2026-08-07" },
  { id: "M-102", name: "Electric Drive Motor M-102", rul_days: 42, fail_prob: 0.22, risk: "Yellow", health: 71.0, next_maint: "2026-08-31" },
  { id: "C-201", name: "Hydrogen Compressor C-201", rul_days: 145, fail_prob: 0.05, risk: "Green", health: 92.0, next_maint: "2026-12-10" },
  { id: "T-301", name: "Feedwater Storage Tank T-301", rul_days: 320, fail_prob: 0.08, risk: "Green", health: 88.0, next_maint: "2027-05-14" }
];

export default function PredictivePage() {
  return (
    <div className="space-y-6 max-w-7xl mx-auto">
      {/* Header */}
      <div className="flex items-center justify-between border-b border-slate-800 pb-4">
        <div>
          <h1 className="text-2xl font-extrabold text-white flex items-center gap-2">
            <Activity className="w-6 h-6 text-amber-400" /> Predictive Maintenance & Failure Heatmap
          </h1>
          <p className="text-xs text-slate-400 mt-0.5">
            Remaining Useful Life (RUL) Forecasting, Failure Probability, and Innovation 2 Risk Heatmap
          </p>
        </div>
      </div>

      {/* Innovation 2: Failure Prediction Heatmap Banner */}
      <div className="glass-panel p-6 rounded-2xl border border-amber-500/40 bg-slate-900/80 space-y-4">
        <div className="flex items-center justify-between">
          <div className="flex items-center gap-2">
            <Flame className="w-5 h-5 text-amber-400" />
            <h2 className="text-base font-bold text-white">Innovation 2: Enterprise Plant Failure Risk Heatmap</h2>
          </div>
          <div className="flex items-center gap-3 text-xs font-mono">
            <span className="flex items-center gap-1.5"><span className="w-3 h-3 rounded bg-emerald-500" /> Green (Normal)</span>
            <span className="flex items-center gap-1.5"><span className="w-3 h-3 rounded bg-amber-500" /> Yellow (Watch)</span>
            <span className="flex items-center gap-1.5"><span className="w-3 h-3 rounded bg-orange-500" /> Orange (Warning)</span>
            <span className="flex items-center gap-1.5"><span className="w-3 h-3 rounded bg-rose-600" /> Red (Critical)</span>
          </div>
        </div>

        {/* Heatmap Layout Grid */}
        <div className="grid grid-cols-1 md:grid-cols-4 gap-4 pt-2">
          <div className="p-4 rounded-xl bg-orange-950/40 border border-orange-500/60 neon-border-rose">
            <div className="flex justify-between text-xs font-mono font-bold text-orange-400">
              <span>BAY-1: BOILER FEED</span>
              <span>ORANGE</span>
            </div>
            <p className="text-sm font-bold text-white mt-2">P-101 Pump & M-102 Motor</p>
            <p className="text-xs text-slate-300 mt-1">RUL: 18 Days • Bearing Vibration 6.8 mm/s</p>
          </div>

          <div className="p-4 rounded-xl bg-rose-950/60 border border-rose-500 neon-border-rose">
            <div className="flex justify-between text-xs font-mono font-bold text-rose-400">
              <span>BAY-2: STEAM HEADER</span>
              <span>CRITICAL RED</span>
            </div>
            <p className="text-sm font-bold text-white mt-2">Valve V-101</p>
            <p className="text-xs text-slate-300 mt-1">RUL: 6 Days • Actuator Friction Friction</p>
          </div>

          <div className="p-4 rounded-xl bg-emerald-950/30 border border-emerald-500/40">
            <div className="flex justify-between text-xs font-mono font-bold text-emerald-400">
              <span>BAY-3: HYDROCRACKER</span>
              <span>GREEN</span>
            </div>
            <p className="text-sm font-bold text-white mt-2">Compressor C-201</p>
            <p className="text-xs text-slate-300 mt-1">RUL: 145 Days • Normal Operation</p>
          </div>

          <div className="p-4 rounded-xl bg-emerald-950/30 border border-emerald-500/40">
            <div className="flex justify-between text-xs font-mono font-bold text-emerald-400">
              <span>BAY-4: TANK FARM</span>
              <span>GREEN</span>
            </div>
            <p className="text-sm font-bold text-white mt-2">Tank T-301</p>
            <p className="text-xs text-slate-300 mt-1">RUL: 320 Days • Shell Thickness OK</p>
          </div>
        </div>
      </div>

      {/* RUL Asset Ranking Table */}
      <div className="glass-panel p-5 rounded-2xl border border-slate-700/60">
        <h3 className="text-base font-bold text-white mb-4 flex items-center gap-2">
          <Calendar className="w-4 h-4 text-cyan-400" /> Remaining Useful Life (RUL) & Maintenance Calendar
        </h3>

        <div className="overflow-x-auto">
          <table className="w-full text-left border-collapse text-xs">
            <thead>
              <tr className="border-b border-slate-800 text-slate-400 font-mono text-[11px]">
                <th className="p-3">Asset ID</th>
                <th className="p-3">Equipment Name</th>
                <th className="p-3">Health Score</th>
                <th className="p-3">RUL (Days)</th>
                <th className="p-3">Failure Prob</th>
                <th className="p-3">Risk Level</th>
                <th className="p-3">Next Scheduled PM</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-slate-800/60">
              {assetHealthList.map((item) => (
                <tr key={item.id} className="hover:bg-slate-900/60 transition-all font-mono">
                  <td className="p-3 font-bold text-cyan-400">{item.id}</td>
                  <td className="p-3 font-sans text-slate-200">{item.name}</td>
                  <td className="p-3 font-bold text-amber-400">{item.health}%</td>
                  <td className="p-3 font-bold text-white">{item.rul_days} Days</td>
                  <td className="p-3 text-slate-300">{(item.fail_prob * 100).toFixed(0)}%</td>
                  <td className="p-3">
                    <span className={`px-2 py-0.5 rounded text-[10px] font-bold ${
                      item.risk === 'Red' ? 'bg-rose-500/20 text-rose-300' : (item.risk === 'Orange' ? 'bg-amber-500/20 text-amber-300' : 'bg-emerald-500/20 text-emerald-300')
                    }`}>
                      {item.risk}
                    </span>
                  </td>
                  <td className="p-3 text-slate-400">{item.next_maint}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}
