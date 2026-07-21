'use client';

import React from 'react';
import { 
  GitCommit, 
  HelpCircle, 
  Clock, 
  CheckCircle2, 
  Wrench, 
  ShieldCheck,
  Zap
} from 'lucide-react';

const fishboneCategories = [
  { category: "Machine", causes: ["Drive-end bearing race pitting", "API Plan 53B pressure orifice wear"] },
  { category: "Method", causes: ["Standard lubrication interval missed by 14 days", "Vibration baseline uncalibrated"] },
  { category: "Material", causes: ["Seal flush oil contamination (0.8% water content)", "Non-OEM gasket sealant used"] },
  { category: "Manpower", causes: ["Turnover in lead technician team", "Field shift handover log incomplete"] },
  { category: "Measurement", causes: ["Analog pressure gauge drift (+0.6 bar)", "SCADA telemetry 15m sampling interval"] },
  { category: "Environment", causes: ["High ambient summer temp (44°C)", "Humidity in auxiliary pump enclosure"] }
];

const fiveWhys = [
  { why: "Why did Pump P-101 fail high vibration limit?", answer: "The drive-end roller bearing developed micro-pitting on its inner race." },
  { why: "Why did the bearing inner race pit?", answer: "The lubricating oil lost film viscosity due to seal fluid dilution." },
  { why: "Why was the oil diluted with seal fluid?", answer: "The mechanical seal throttle bushing leaked pressure under transient loads." },
  { why: "Why did the seal bushing leak?", answer: "The flush plan accumulator pressure dropped below suction pressure." },
  { why: "Why did accumulator pressure drop?", answer: "ROOT CAUSE: Nitrogen bladder pre-charge was not checked during the Q2 preventive maintenance cycle." }
];

export default function RCAPage() {
  return (
    <div className="space-y-6 max-w-7xl mx-auto">
      {/* Header */}
      <div className="flex items-center justify-between border-b border-slate-800 pb-4">
        <div>
          <h1 className="text-2xl font-extrabold text-white flex items-center gap-2">
            <GitCommit className="w-6 h-6 text-purple-400" /> Root Cause Analysis (RCA) Agent
          </h1>
          <p className="text-xs text-slate-400 mt-0.5">
            Automated Ishikawa Fishbone Diagram, 5-Why Deductive Tree, and Corrective Action Plan
          </p>
        </div>
      </div>

      {/* Fishbone Ishikawa Diagram Renderer */}
      <div className="glass-panel p-6 rounded-2xl border border-purple-500/30 space-y-4">
        <h2 className="text-base font-bold text-white flex items-center gap-2">
          <Wrench className="w-4 h-4 text-purple-400" /> Ishikawa (Fishbone) Diagram - Incident P-101
        </h2>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-4 pt-2">
          {fishboneCategories.map((cat, idx) => (
            <div key={idx} className="glass-card p-4 rounded-xl border border-slate-700/80 bg-slate-900/60">
              <span className="text-xs font-bold text-purple-400 uppercase font-mono tracking-wider">{cat.category}</span>
              <ul className="mt-2 space-y-1.5">
                {cat.causes.map((c, i) => (
                  <li key={i} className="text-xs text-slate-300 flex items-start gap-1.5">
                    <span className="w-1.5 h-1.5 rounded-full bg-purple-400 mt-1.5" />
                    <span>{c}</span>
                  </li>
                ))}
              </ul>
            </div>
          ))}
        </div>
      </div>

      {/* 5-Why Analysis Tree */}
      <div className="glass-panel p-6 rounded-2xl border border-slate-700/60 space-y-4">
        <h2 className="text-base font-bold text-white flex items-center gap-2">
          <HelpCircle className="w-4 h-4 text-cyan-400" /> 5-Why Deductive Reasoning Tree
        </h2>

        <div className="space-y-3 font-mono text-xs">
          {fiveWhys.map((item, idx) => (
            <div key={idx} className={`p-4 rounded-xl border ${
              idx === 4 ? 'bg-amber-950/40 border-amber-500/60 text-amber-300 neon-border-cyan' : 'bg-slate-900/80 border-slate-800 text-slate-300'
            }`}>
              <div className="font-bold text-cyan-400 mb-1">Step {idx + 1}: {item.why}</div>
              <div className="text-slate-200 font-sans">{item.answer}</div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
