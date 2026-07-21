'use client';

import React, { useState } from 'react';
import Link from 'next/link';
import { 
  UploadCloud, 
  Sparkles, 
  FileText, 
  CheckCircle2, 
  Loader2, 
  Boxes, 
  Users, 
  ShieldAlert, 
  ArrowRight, 
  RefreshCw, 
  Bot, 
  Database, 
  Dna,
  Network,
  Cpu
} from 'lucide-react';
import { useWorkspace, PIPELINE_STEPS } from '@/context/WorkspaceContext';

export default function WorkspaceLandingPage() {
  const { 
    isLoaded, 
    isProcessing, 
    processingStep, 
    uploadedFiles, 
    extractedAssets, 
    detectedEngineers, 
    riskFindings, 
    complianceIssues, 
    loadGenChemDataset, 
    uploadCustomFiles, 
    resetWorkspace 
  } = useWorkspace();

  const [dragActive, setDragActive] = useState(false);

  const handleDragOver = (e: React.DragEvent) => {
    e.preventDefault();
    setDragActive(true);
  };

  const handleDragLeave = () => {
    setDragActive(false);
  };

  const handleDrop = (e: React.DragEvent) => {
    e.preventDefault();
    setDragActive(false);
    if (e.dataTransfer.files && e.dataTransfer.files.length > 0) {
      uploadCustomFiles(Array.from(e.dataTransfer.files));
    }
  };

  const handleFileInput = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files && e.target.files.length > 0) {
      uploadCustomFiles(Array.from(e.target.files));
    }
  };

  return (
    <div className="max-w-6xl mx-auto space-y-8 font-sans pb-12">
      {/* Top Header Banner */}
      <div className="text-center md:text-left space-y-2 pt-2 border-b border-stone-200 pb-6 flex items-center justify-between">
        <div>
          <h1 className="text-3xl font-extrabold text-stone-900 tracking-tight font-sans">
            Industrial Brain <span className="text-blue-600">Operations Workspace</span>
          </h1>
          <p className="text-sm text-stone-600 font-sans">
            Ingest plant telemetry, engineering documents, construct living Knowledge Graphs, and run multi-agent predictive intelligence.
          </p>
        </div>

        {isLoaded && (
          <button
            onClick={resetWorkspace}
            className="inline-flex items-center gap-2 px-4 py-2 rounded-lg bg-stone-100 hover:bg-stone-200 text-stone-800 text-xs font-mono font-bold border border-stone-300 transition-all shadow-xs"
          >
            <RefreshCw className="w-3.5 h-3.5" />
            Reset Workspace
          </button>
        )}
      </div>

      {/* Main Workspace Ingestion Hero Card */}
      {!isLoaded && !isProcessing && (
        <div className="space-y-8">
          <div
            onDragOver={handleDragOver}
            onDragLeave={handleDragLeave}
            onDrop={handleDrop}
            className={`bg-white p-10 rounded-2xl border-2 border-dashed text-center transition-all duration-200 shadow-xs ${
              dragActive 
                ? 'border-blue-600 bg-blue-50/50 scale-[1.01]' 
                : 'border-stone-300 hover:border-stone-400 bg-white'
            }`}
          >
            <div className="w-16 h-16 mx-auto rounded-2xl bg-blue-50 border border-blue-100 flex items-center justify-center mb-4">
              <UploadCloud className="w-8 h-8 text-blue-600" />
            </div>

            <h2 className="text-xl font-bold text-stone-900 font-sans">
              Ingest Plant Engineering Documents & Telemetry
            </h2>
            <p className="text-xs text-stone-500 max-w-lg mx-auto mt-2 font-sans">
              Drag and drop your engineering PDF manuals, P&ID drawings, incident reports, or telemetry CSV logs here to trigger automated Knowledge Graph synthesis.
            </p>

            <div className="flex items-center justify-center gap-2 my-5">
              {['.PDF', '.DOCX', '.XLSX', '.CSV', '.P&ID'].map((fmt) => (
                <span key={fmt} className="px-3 py-1 rounded bg-stone-100 border border-stone-200 text-[10px] font-mono text-stone-700 font-bold">
                  {fmt}
                </span>
              ))}
            </div>

            <div className="flex flex-col sm:flex-row items-center justify-center gap-4 mt-6">
              <label className="cursor-pointer inline-flex items-center gap-2 px-6 py-3 rounded-xl bg-slate-900 hover:bg-slate-800 text-white text-xs font-bold font-sans transition-all shadow-md">
                <FileText className="w-4 h-4 text-blue-400" />
                Select Local File
                <input type="file" multiple onChange={handleFileInput} className="hidden" />
              </label>

              <span className="text-xs text-stone-400 font-mono">OR</span>

              <button
                onClick={loadGenChemDataset}
                className="inline-flex items-center gap-2 px-6 py-3 rounded-xl bg-blue-600 hover:bg-blue-700 text-white text-xs font-bold font-sans transition-all shadow-md"
              >
                <Sparkles className="w-4 h-4 text-yellow-300" />
                Ingest GenChem Refinery Master Dataset
              </button>
            </div>

            <p className="text-[11px] text-stone-400 font-mono mt-4">
              One-click dataset demo populates 130 assets, P&ID schematics, 70+ documents, and live telemetry logs.
            </p>
          </div>

          {/* Platform Capability Showcase */}
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 pt-4">
            <div className="bg-white p-5 rounded-xl border border-stone-200 space-y-2">
              <div className="w-9 h-9 rounded-lg bg-blue-50 border border-blue-100 flex items-center justify-center">
                <FileText className="w-4 h-4 text-blue-600" />
              </div>
              <h3 className="text-xs font-bold text-stone-900 font-mono">1. Document Intelligence</h3>
              <p className="text-[11px] text-stone-500 font-sans leading-relaxed">
                Auto-OCR, layout parsing, and bounding-box tag extraction for P&ID schematics.
              </p>
            </div>

            <div className="bg-white p-5 rounded-xl border border-stone-200 space-y-2">
              <div className="w-9 h-9 rounded-lg bg-purple-50 border border-purple-100 flex items-center justify-center">
                <Network className="w-4 h-4 text-purple-600" />
              </div>
              <h3 className="text-xs font-bold text-stone-900 font-mono">2. Living Knowledge Graph</h3>
              <p className="text-[11px] text-stone-500 font-sans leading-relaxed">
                Multi-hop graph linkage connecting equipment, engineers, manuals, and failure codes.
              </p>
            </div>

            <div className="bg-white p-5 rounded-xl border border-stone-200 space-y-2">
              <div className="w-9 h-9 rounded-lg bg-emerald-50 border border-emerald-100 flex items-center justify-center">
                <Cpu className="w-4 h-4 text-emerald-600" />
              </div>
              <h3 className="text-xs font-bold text-stone-900 font-mono">3. Multi-Agent Swarm</h3>
              <p className="text-[11px] text-stone-500 font-sans leading-relaxed">
                Autonomous collaboration between RCA, Compliance, Audit, and Maintenance agents.
              </p>
            </div>

            <div className="bg-white p-5 rounded-xl border border-stone-200 space-y-2">
              <div className="w-9 h-9 rounded-lg bg-amber-50 border border-amber-100 flex items-center justify-center">
                <Boxes className="w-4 h-4 text-amber-600" />
              </div>
              <h3 className="text-xs font-bold text-stone-900 font-mono">4. Digital Twin & RUL</h3>
              <p className="text-[11px] text-stone-500 font-sans leading-relaxed">
                Weibull curve degradation forecasts, remaining useful life, and equipment chatbot.
              </p>
            </div>
          </div>
        </div>
      )}

      {/* Live Processing Pipeline Animation */}
      {isProcessing && (
        <div className="bg-white p-8 rounded-2xl border border-stone-200 space-y-6 shadow-xs">
          <div className="flex items-center justify-between">
            <div>
              <span className="text-xs font-mono font-bold text-blue-600 uppercase tracking-widest">
                AI Processing Pipeline
              </span>
              <h2 className="text-lg font-bold text-stone-900 mt-1 font-sans">
                Constructing Industrial Knowledge Graph...
              </h2>
            </div>
            <Loader2 className="w-6 h-6 text-blue-600 animate-spin" />
          </div>

          <div className="w-full bg-stone-100 rounded-full h-2 overflow-hidden border border-stone-200">
            <div
              className="bg-blue-600 h-full transition-all duration-300"
              style={{ width: `${((processingStep + 1) / PIPELINE_STEPS.length) * 100}%` }}
            />
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-3 pt-2">
            {PIPELINE_STEPS.map((stepName, idx) => {
              const isDone = idx < processingStep;
              const isCurrent = idx === processingStep;

              return (
                <div
                  key={stepName}
                  className={`p-3.5 rounded-xl border flex items-center justify-between text-xs font-mono transition-all ${
                    isDone
                      ? 'bg-stone-100 border-stone-200 text-stone-700 font-semibold'
                      : isCurrent
                      ? 'bg-blue-600 text-white font-extrabold border-blue-600 shadow-md'
                      : 'bg-white border-stone-200 text-stone-400'
                  }`}
                >
                  <span className="truncate">{idx + 1}. {stepName}</span>
                  {isDone && <CheckCircle2 className="w-4 h-4 text-emerald-600 shrink-0" />}
                  {isCurrent && <Loader2 className="w-4 h-4 text-white animate-spin shrink-0" />}
                </div>
              );
            })}
          </div>
        </div>
      )}

      {/* Analysis Summary Dashboard */}
      {isLoaded && !isProcessing && (
        <div className="space-y-6">
          <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
            <div className="bg-white p-4 rounded-xl border border-stone-200 flex items-center gap-3">
              <div className="w-9 h-9 rounded-lg bg-blue-50 border border-blue-100 flex items-center justify-center">
                <Boxes className="w-4 h-4 text-blue-600" />
              </div>
              <div>
                <p className="text-[10px] text-stone-500 font-mono uppercase">Assets Detected</p>
                <p className="text-lg font-black text-stone-900 font-mono">{extractedAssets.length}</p>
              </div>
            </div>

            <div className="bg-white p-4 rounded-xl border border-stone-200 flex items-center gap-3">
              <div className="w-9 h-9 rounded-lg bg-stone-100 border border-stone-200 flex items-center justify-center">
                <Users className="w-4 h-4 text-stone-700" />
              </div>
              <div>
                <p className="text-[10px] text-stone-500 font-mono uppercase">Engineers Found</p>
                <p className="text-lg font-black text-stone-900 font-mono">{detectedEngineers.length}</p>
              </div>
            </div>

            <div className="bg-white p-4 rounded-xl border border-stone-200 flex items-center gap-3">
              <div className="w-9 h-9 rounded-lg bg-amber-50 border border-amber-200 flex items-center justify-center">
                <ShieldAlert className="w-4 h-4 text-amber-600" />
              </div>
              <div>
                <p className="text-[10px] text-stone-500 font-mono uppercase">Active Risks</p>
                <p className="text-lg font-black text-stone-900 font-mono">{riskFindings.length}</p>
              </div>
            </div>

            <div className="bg-white p-4 rounded-xl border border-stone-200 flex items-center gap-3">
              <div className="w-9 h-9 rounded-lg bg-stone-100 border border-stone-200 flex items-center justify-center">
                <FileText className="w-4 h-4 text-stone-700" />
              </div>
              <div>
                <p className="text-[10px] text-stone-500 font-mono uppercase">Docs Ingested</p>
                <p className="text-lg font-black text-stone-900 font-mono">{uploadedFiles.length}</p>
              </div>
            </div>
          </div>

          <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
            <div className="bg-white p-6 rounded-2xl border border-stone-200 space-y-4">
              <h3 className="text-sm font-bold text-stone-900 flex items-center gap-2 font-mono">
                <Boxes className="w-4 h-4 text-blue-600" />
                Detected Equipment DNA ({extractedAssets.length})
              </h3>

              <div className="space-y-3">
                {extractedAssets.map((asset) => (
                  <div key={asset.id} className="p-3 rounded-xl bg-stone-50 border border-stone-200 flex items-center justify-between">
                    <div>
                      <span className="text-[10px] font-mono bg-blue-50 text-blue-700 px-2 py-0.5 rounded border border-blue-200 font-bold">
                        {asset.id}
                      </span>
                      <h4 className="text-xs font-bold text-stone-900 mt-1 font-mono">{asset.name}</h4>
                      <p className="text-[10px] text-stone-500 font-mono">{asset.location}</p>
                    </div>
                    <div className="text-right">
                      <span className="text-xs font-mono font-bold text-stone-900">{asset.health}% Health</span>
                      <p className="text-[10px] text-stone-500 font-mono">RUL: {asset.rul} Days</p>
                    </div>
                  </div>
                ))}
              </div>
            </div>

            <div className="bg-white p-6 rounded-2xl border border-stone-200 space-y-4">
              <h3 className="text-sm font-bold text-stone-900 flex items-center gap-2 font-mono">
                <ShieldAlert className="w-4 h-4 text-amber-600" />
                Identified Risk & Compliance Gaps
              </h3>

              <div className="space-y-3">
                {riskFindings.map((risk, idx) => (
                  <div key={idx} className="p-3 rounded-xl bg-stone-50 border border-stone-200 space-y-1 font-mono">
                    <span className="text-[10px] text-amber-700 font-bold uppercase">{risk.asset} • {risk.severity} Severity</span>
                    <h4 className="text-xs font-bold text-stone-900">{risk.title}</h4>
                    <p className="text-[11px] text-stone-600">{risk.detail}</p>
                  </div>
                ))}

                {complianceIssues.map((comp, idx) => (
                  <div key={idx} className="p-3 rounded-xl bg-stone-50 border border-stone-200 space-y-1 font-mono">
                    <span className="text-[10px] text-stone-600 font-bold uppercase">{comp.standard} Gap</span>
                    <h4 className="text-xs font-bold text-stone-900">{comp.requirement}</h4>
                    <p className="text-[11px] text-stone-600">{comp.status}</p>
                  </div>
                ))}
              </div>
            </div>

            <div className="bg-white p-6 rounded-2xl border border-stone-200 space-y-4">
              <h3 className="text-sm font-bold text-stone-900 flex items-center gap-2 font-mono">
                <Sparkles className="w-4 h-4 text-blue-600" />
                Next Recommended Actions
              </h3>

              <div className="space-y-3">
                <Link
                  href="/copilot"
                  className="block p-4 rounded-xl bg-stone-50 border border-stone-200 hover:border-blue-600 transition-all group font-mono"
                >
                  <div className="flex items-center justify-between">
                    <div className="flex items-center gap-2">
                      <Bot className="w-4 h-4 text-blue-600" />
                      <span className="text-xs font-bold text-stone-900">Query Evidence Copilot</span>
                    </div>
                    <ArrowRight className="w-4 h-4 text-blue-600 group-hover:translate-x-1 transition-transform" />
                  </div>
                  <p className="text-[11px] text-stone-600 mt-1">Ask specific questions about uploaded documents.</p>
                </Link>

                <Link
                  href="/graph"
                  className="block p-4 rounded-xl bg-stone-50 border border-stone-200 hover:border-blue-600 transition-all group font-mono"
                >
                  <div className="flex items-center justify-between">
                    <div className="flex items-center gap-2">
                      <Database className="w-4 h-4 text-stone-700" />
                      <span className="text-xs font-bold text-stone-900">Explore Knowledge Graph</span>
                    </div>
                    <ArrowRight className="w-4 h-4 text-stone-700 group-hover:translate-x-1 transition-transform" />
                  </div>
                  <p className="text-[11px] text-stone-600 mt-1">Visualize multi-hop topology and drag Time Travel timeline.</p>
                </Link>

                <Link
                  href="/digital-twin"
                  className="block p-4 rounded-xl bg-stone-50 border border-stone-200 hover:border-blue-600 transition-all group font-mono"
                >
                  <div className="flex items-center justify-between">
                    <div className="flex items-center gap-2">
                      <Dna className="w-4 h-4 text-stone-700" />
                      <span className="text-xs font-bold text-stone-900">Inspect Equipment DNA</span>
                    </div>
                    <ArrowRight className="w-4 h-4 text-stone-700 group-hover:translate-x-1 transition-transform" />
                  </div>
                  <p className="text-[11px] text-stone-600 mt-1">Review lifetime maintenance, Weibull RUL, and machine chatbot.</p>
                </Link>
              </div>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}

