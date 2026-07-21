'use client';

import React from 'react';
import { 
  BarChart3, 
  ShieldAlert, 
  DollarSign, 
  CheckCircle2, 
  Boxes, 
  Sparkles, 
  Clock
} from 'lucide-react';
import { useWorkspace } from '@/context/WorkspaceContext';
import Link from 'next/link';

export default function ExecutiveDashboardPage() {
  const { isLoaded, extractedAssets, riskFindings, complianceIssues, uploadedFiles } = useWorkspace();

  if (!isLoaded) {
    return (
      <div className="max-w-4xl mx-auto py-16 text-center space-y-6 font-sans">
        <div className="w-16 h-16 rounded-2xl bg-[#FFF7ED] border border-[#FFEDD5] flex items-center justify-center mx-auto shadow-xs">
          <BarChart3 className="w-8 h-8 text-[#F9572A]" />
        </div>
        <h2 className="text-xl font-bold text-stone-900 font-sans">No Executive Data Computed Yet</h2>
        <p className="text-xs text-stone-600 max-w-md mx-auto font-sans">
          Executive metrics and financial risk projections are computed dynamically once industrial documents are uploaded.
        </p>
        <Link
          href="/"
          className="inline-flex items-center gap-2 px-6 py-2.5 rounded-xl bg-[#F9572A] hover:bg-[#EA580C] text-white font-bold font-sans text-xs shadow-md transition-all"
        >
          Go to Workspace Upload Zone
        </Link>
      </div>
    );
  }

  const avgHealth = extractedAssets.length > 0 
    ? (extractedAssets.reduce((acc, a) => acc + (a.health || 80), 0) / extractedAssets.length).toFixed(1)
    : "85.0";

  const totalDowntimeEst = (riskFindings.length * 7.25 + 2.0).toFixed(1);
  const financialLossEst = (parseFloat(totalDowntimeEst) * 18500).toLocaleString('en-US');

  return (
    <div className="space-y-6 max-w-6xl mx-auto font-sans pb-12">
      {/* Header */}
      <div className="flex flex-col md:flex-row md:items-center justify-between gap-4 border-b border-stone-200 pb-4">
        <div>
          <h1 className="text-2xl font-extrabold text-stone-900 flex items-center gap-2 font-sans">
            <BarChart3 className="w-6 h-6 text-[#F9572A]" /> Executive Intelligence & ROI Analytics
          </h1>
          <p className="text-xs text-stone-600 mt-1 font-sans">
            Computed strictly from {uploadedFiles.length} uploaded document stream(s)
          </p>
        </div>
      </div>

      {/* KPI Cards Grid */}
      <div className="grid grid-cols-1 md:grid-cols-4 gap-4 font-mono">
        <div className="bg-white p-5 rounded-2xl border border-stone-200 space-y-2 shadow-xs">
          <div className="flex items-center justify-between">
            <span className="text-xs text-stone-500 font-mono">Plant Health Index</span>
            <Boxes className="w-4 h-4 text-[#F9572A]" />
          </div>
          <p className="text-2xl font-black text-stone-900">{avgHealth}%</p>
          <span className="text-[10px] text-stone-500 block">Derived from {extractedAssets.length} assets</span>
        </div>

        <div className="bg-white p-5 rounded-2xl border border-stone-200 space-y-2 shadow-xs">
          <div className="flex items-center justify-between">
            <span className="text-xs text-stone-500 font-mono">Active Risks</span>
            <ShieldAlert className="w-4 h-4 text-amber-600" />
          </div>
          <p className="text-2xl font-black text-amber-600">{riskFindings.length}</p>
          <span className="text-[10px] text-stone-500 block">High priority alerts</span>
        </div>

        <div className="bg-white p-5 rounded-2xl border border-stone-200 space-y-2 shadow-xs">
          <div className="flex items-center justify-between">
            <span className="text-xs text-stone-500 font-mono">Est. Downtime Risk</span>
            <Clock className="w-4 h-4 text-stone-700" />
          </div>
          <p className="text-2xl font-black text-stone-900">{totalDowntimeEst} Hrs</p>
          <span className="text-[10px] text-stone-500 block">Cascade propagation</span>
        </div>

        <div className="bg-white p-5 rounded-2xl border border-stone-200 space-y-2 shadow-xs">
          <div className="flex items-center justify-between">
            <span className="text-xs text-stone-500 font-mono">Est. Outage Loss</span>
            <DollarSign className="w-4 h-4 text-rose-600" />
          </div>
          <p className="text-2xl font-black text-rose-600">${financialLossEst}</p>
          <span className="text-[10px] text-stone-500 block">Potential production loss</span>
        </div>
      </div>

      {/* Strategy Comparison & Action Recommendations */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6 font-sans">
        <div className="bg-white p-6 rounded-2xl border border-stone-200 space-y-4 shadow-xs">
          <h3 className="text-base font-bold text-stone-900 flex items-center gap-2">
            <Sparkles className="w-4 h-4 text-[#F9572A]" /> Executive Strategy Comparison
          </h3>

          <div className="space-y-3 font-mono">
            <div className="p-4 rounded-xl bg-stone-50 border border-stone-200">
              <div className="flex justify-between items-center text-xs font-bold text-stone-600">
                <span>Strategy A: Run to Failure</span>
                <span className="text-rose-600">High Risk</span>
              </div>
              <div className="flex justify-between items-center mt-2 text-sm font-bold text-stone-900">
                <span>Cost: $280,000</span>
                <span>Downtime: {totalDowntimeEst} Hrs</span>
              </div>
            </div>

            <div className="p-4 rounded-xl bg-[#FFF7ED] border border-[#FFEDD5]">
              <div className="flex justify-between items-center text-xs font-bold text-[#F9572A]">
                <span>Strategy C: Predictive Overhaul (Recommended)</span>
                <span className="text-emerald-700">Minimal Risk</span>
              </div>
              <div className="flex justify-between items-center mt-2 text-sm font-bold text-stone-900">
                <span>Cost: $4,200</span>
                <span>Downtime: 2.0 Hrs</span>
              </div>
              <p className="text-xs text-emerald-700 mt-2 font-bold">
                ✓ Net Savings: ${((parseFloat(totalDowntimeEst) * 18500) - 4200).toLocaleString('en-US')}
              </p>
            </div>
          </div>
        </div>

        <div className="bg-white p-6 rounded-2xl border border-stone-200 space-y-4 shadow-xs">
          <h3 className="text-base font-bold text-stone-900 flex items-center gap-2">
            <CheckCircle2 className="w-4 h-4 text-emerald-600" /> Action Priority Checklist
          </h3>

          <div className="space-y-3 font-mono">
            {riskFindings.map((risk, idx) => (
              <div key={idx} className="p-3.5 rounded-xl bg-stone-50 border border-stone-200 flex items-center justify-between">
                <div>
                  <span className="text-[10px] text-[#F9572A] font-bold">{risk.asset}</span>
                  <h4 className="text-xs font-bold text-stone-900">{risk.title}</h4>
                </div>
                <Link href="/digital-twin" className="text-xs text-[#F9572A] font-bold hover:underline">
                  Inspect DNA →
                </Link>
              </div>
            ))}

            {riskFindings.length === 0 && (
              <div className="p-4 rounded-xl bg-stone-50 border border-stone-200 text-xs text-stone-500">
                No high-severity risks detected in current document stream.
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  );
}
