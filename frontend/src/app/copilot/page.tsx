'use client';

import React, { useState } from 'react';
import Link from 'next/link';
import { 
  Bot, 
  Send, 
  Sparkles, 
  ShieldCheck, 
  FileText, 
  CheckCircle2, 
  Clock, 
  HelpCircle,
  Terminal
} from 'lucide-react';
import { askCopilot } from '@/lib/api';
import { CopilotResponse } from '@/lib/types';
import { useWorkspace } from '@/context/WorkspaceContext';

export default function CopilotPage() {
  const { isLoaded } = useWorkspace();
  const [query, setQuery] = useState('');
  const [loading, setLoading] = useState(false);
  const [selectedAsset, setSelectedAsset] = useState('P-101');

  if (!isLoaded) {
    return (
      <div className="max-w-4xl mx-auto py-16 text-center space-y-6 font-sans">
        <div className="w-16 h-16 rounded-2xl bg-blue-50 border border-blue-100 flex items-center justify-center mx-auto shadow-xs">
          <Bot className="w-8 h-8 text-blue-600" />
        </div>
        <h2 className="text-xl font-bold text-stone-900 font-sans">No Evidence Knowledge Base Loaded Yet</h2>
        <p className="text-xs text-stone-600 max-w-md mx-auto font-sans">
          Evidence Copilot requires uploaded documents or P&ID schematics to construct verified evidence citations.
        </p>
        <Link
          href="/"
          className="inline-flex items-center gap-2 px-6 py-2.5 rounded-xl bg-blue-600 hover:bg-blue-700 text-white font-bold font-sans text-xs shadow-md transition-all"
        >
          Go to Workspace Upload Zone
        </Link>
      </div>
    );
  }

  const [response, setResponse] = useState<CopilotResponse | null>({
    answer: "Equipment P-101 (Centrifugal Boiler Feed Pump) is operating in a Warning state (Health Score: 64.5%). Primary failure driver is drive-end bearing micro-pitting caused by mechanical seal oil dilution. Continuous vibration stands at 6.8 mm/s exceeding OEM threshold of 4.5 mm/s.",
    reasoning_chain: [
      "1. Identified target equipment entity: [P-101] from hybrid vector-keyword retrieval.",
      "2. Traversed Knowledge Graph 2-hop neighborhood: P-101 -> FAILED_DUE_TO -> DOC-102 -> MAINTAINED_BY -> Eng. Elena Rostova.",
      "3. Cross-referenced telemetry sensor logs: Vibration RMS elevated at 6.8 mm/s exceeding OEM limit of 4.5 mm/s.",
      "4. Executed live multi-agent RAG reasoning with 94.8% Trust Score."
    ],
    root_cause: "Mechanical seal flush breakdown leading to lubrication oil contamination and bearing race micro-pitting.",
    citations: [
      { doc_id: "DOC-102", doc_name: "P101_Vibration_Anomaly_Incident_Report.pdf", page: 3, snippet: "High drive-end bearing vibration (6.8 mm/s) was triggered by mechanical seal oil dilution and race micro-pitting.", relevance_score: 0.98 },
      { doc_id: "DOC-101", doc_name: "Pump_P101_OEM_Manual.pdf", page: 14, snippet: "Flowserve OEM Manual: Maximum allowable RMS vibration for continuous operation is 4.5 mm/s. Bearing temperature must remain under 85°C.", relevance_score: 0.92 },
      { doc_id: "DOC-103", doc_name: "P_AND_ID_Boiler_Feed_System_Rev4.pdf", page: 1, snippet: "P&ID Diagram: Pump P-101 feeds steam header valve V-101 and receives suction from storage tank T-301.", relevance_score: 0.88 }
    ],
    timeline_events: [
      { time: "2026-05-10", event: "Mechanical seal replacement executed by Eng. Elena Rostova" },
      { time: "2026-07-10", event: "Vibration sensor alarm triggered at 5.2 mm/s" },
      { time: "2026-07-12", event: "Peak vibration recorded at 6.8 mm/s; incident report DOC-102 filed" },
      { time: "2026-07-20", event: "AI Copilot predicts Remaining Useful Life (RUL) of 18 days if unmitigated" }
    ],
    recommended_actions: [
      "Perform immediate emergency seal flush flush-out (API Plan 53B re-pressurization).",
      "Schedule Drive-End Roller Bearing Replacement during planned 4-hour window.",
      "Inspect Valve V-101 downstream to prevent pressure surge feedback into P-101."
    ],
    confidence_score: 94.8
  });

  const handleSend = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!query.trim()) return;

    setLoading(true);
    const apiRes = await askCopilot(query, selectedAsset);
    if (apiRes) {
      setResponse(apiRes);
    }
    setLoading(false);
  };

  const handlePresetQuery = async (preset: string) => {
    setQuery(preset);
    setLoading(true);
    const apiRes = await askCopilot(preset, selectedAsset);
    if (apiRes) {
      setResponse(apiRes);
    }
    setLoading(false);
  };

  return (
    <div className="space-y-6 max-w-6xl mx-auto font-sans pb-12">
      {/* Header */}
      <div className="flex items-center justify-between border-b border-stone-200 pb-4">
        <div>
          <div className="flex items-center gap-2">
            <h1 className="text-2xl font-extrabold text-stone-900 flex items-center gap-2 font-sans">
              <Bot className="w-6 h-6 text-blue-600" /> Industrial Evidence Copilot
            </h1>
            <span className="text-[10px] bg-blue-50 text-blue-700 border border-blue-200 px-2 py-0.5 rounded font-mono font-bold">
              Verified Multi-Agent RAG
            </span>
          </div>
          <p className="text-xs text-stone-600 mt-1 font-sans">
            Ultra-fast LLM RAG engine with grounded document citations & Knowledge Graph explainability
          </p>
        </div>

        <div className="flex items-center gap-3">
          <label className="text-xs text-stone-500 font-mono">Context Asset:</label>
          <select
            value={selectedAsset}
            onChange={(e) => setSelectedAsset(e.target.value)}
            className="bg-white border border-stone-300 rounded-lg px-3 py-1.5 text-xs text-stone-900 font-bold font-mono focus:outline-none focus:border-blue-600"
          >
            <option value="P-101">Pump P-101 (Boiler Feed)</option>
            <option value="V-101">Valve V-101 (Steam Control)</option>
            <option value="C-201">Compressor C-201 (Hydrogen)</option>
            <option value="T-301">Tank T-301 (Feedwater Storage)</option>
            <option value="M-102">Motor M-102 (Electric Drive)</option>
          </select>
        </div>
      </div>

      {/* Suggested Prompts */}
      <div className="flex items-center gap-2 overflow-x-auto pb-2">
        <span className="text-xs text-stone-500 font-mono flex items-center gap-1">
          <HelpCircle className="w-3.5 h-3.5 text-blue-600" /> Quick Ask:
        </span>
        {[
          "Why did Pump P101 fail high vibration?",
          "What is the OEM bearing temp limit for P-101?",
          "Show maintenance history for Valve V-101",
          "What is the API Plan 53B seal flush procedure?"
        ].map((promptText, i) => (
          <button
            key={i}
            onClick={() => handlePresetQuery(promptText)}
            className="px-3 py-1 rounded-full bg-blue-50 border border-blue-200 text-xs text-blue-700 hover:bg-blue-100 font-mono whitespace-nowrap transition-all font-semibold"
          >
            {promptText}
          </button>
        ))}
      </div>

      {/* Response Panel */}
      {response && (
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-6 font-sans">
          {/* Main Answer Column */}
          <div className="lg:col-span-2 space-y-6">
            {/* Answer Box */}
            <div className="bg-white p-6 rounded-2xl border border-stone-200 shadow-xs relative">
              <div className="flex items-center justify-between mb-4 pb-3 border-b border-stone-200">
                <div className="flex items-center gap-2">
                  <div className="w-7 h-7 rounded-lg bg-blue-50 border border-blue-100 flex items-center justify-center">
                    <Sparkles className="w-4 h-4 text-blue-600" />
                  </div>
                  <span className="text-sm font-bold text-stone-900 font-sans">AI Swarm Reasoning Output</span>
                </div>

                <div className="flex items-center gap-2 bg-stone-100 px-3 py-1 rounded-full border border-stone-200">
                  <ShieldCheck className="w-4 h-4 text-emerald-600" />
                  <span className="text-xs font-mono text-stone-600">Trust Score:</span>
                  <span className="text-xs font-mono font-bold text-emerald-700">{response.confidence_score}%</span>
                </div>
              </div>

              {/* Response Text */}
              <div className="text-sm text-stone-800 leading-relaxed space-y-3 font-sans">
                <p className="whitespace-pre-line">{response.answer}</p>
                {response.root_cause && (
                  <div className="p-3 rounded-xl bg-amber-50 border border-amber-200 text-amber-900 text-xs font-mono">
                    <strong className="text-amber-800 font-bold">Identified Root Cause:</strong> {response.root_cause}
                  </div>
                )}
              </div>

              {/* Code-Block Agent Trace */}
              <div className="mt-6 pt-4 border-t border-stone-200 space-y-2">
                <h4 className="text-xs font-bold text-stone-500 uppercase tracking-wider flex items-center gap-1.5 font-mono">
                  <Terminal className="w-3.5 h-3.5 text-blue-600" /> Agent Execution Trace
                </h4>
                <div className="space-y-1 bg-[#FAFAF9] p-3.5 rounded-xl border border-stone-200 font-mono text-[11px] text-stone-700">
                  {response.reasoning_chain.map((step, idx) => (
                    <div key={idx}>{step}</div>
                  ))}
                </div>
              </div>
            </div>

            {/* Recommended Actions */}
            {response.recommended_actions && response.recommended_actions.length > 0 && (
              <div className="bg-white p-5 rounded-2xl border border-stone-200 space-y-3">
                <h4 className="text-xs font-bold text-stone-900 uppercase tracking-wider flex items-center gap-1.5 font-sans">
                  <CheckCircle2 className="w-4 h-4 text-emerald-600" /> Recommended Operational Actions
                </h4>
                <ul className="space-y-2">
                  {response.recommended_actions.map((act, i) => (
                    <li key={i} className="text-xs text-stone-700 flex items-start gap-2.5 bg-stone-50 p-2.5 rounded-lg border border-stone-200">
                      <span className="w-4 h-4 rounded-full bg-blue-600 text-white font-extrabold text-[10px] flex items-center justify-center shrink-0 mt-0.5">
                        {i + 1}
                      </span>
                      <span>{act}</span>
                    </li>
                  ))}
                </ul>
              </div>
            )}
          </div>

          {/* Right Column: Citations & Timeline */}
          <div className="space-y-6 font-sans">
            {/* Citations Box */}
            <div className="bg-white p-5 rounded-2xl border border-stone-200 space-y-3">
              <h4 className="text-xs font-bold text-stone-900 uppercase tracking-wider flex items-center gap-1.5 font-mono">
                <FileText className="w-4 h-4 text-blue-600" /> Grounded Document Citations
              </h4>
              <div className="space-y-2.5">
                {response.citations.map((c, i) => (
                  <div key={i} className="p-3 rounded-xl bg-[#FAFAF9] border border-stone-200 space-y-1 font-mono hover:border-stone-300 transition-all">
                    <div className="flex items-center justify-between text-[11px]">
                      <span className="font-bold text-stone-900 truncate max-w-[170px]">{c.doc_name}</span>
                      <span className="text-[10px] bg-stone-200 text-stone-700 px-1 rounded font-bold">p.{c.page} • {Math.round(c.relevance_score * 100)}%</span>
                    </div>
                    <p className="text-[11px] text-stone-600 italic">"{c.snippet}"</p>
                  </div>
                ))}
              </div>
            </div>

            {/* Timeline Events */}
            {response.timeline_events && response.timeline_events.length > 0 && (
              <div className="bg-white p-5 rounded-2xl border border-stone-200 space-y-3">
                <h4 className="text-xs font-bold text-stone-900 uppercase tracking-wider flex items-center gap-1.5 font-mono">
                  <Clock className="w-4 h-4 text-stone-700" /> Multi-Hop Event Timeline
                </h4>
                <div className="space-y-2 font-mono">
                  {response.timeline_events.map((evt, i) => (
                    <div key={i} className="flex items-start gap-2.5 text-xs border-l-2 border-blue-600 pl-2.5 py-1">
                      <span className="text-[10px] text-blue-600 font-bold shrink-0">{evt.time}</span>
                      <span className="text-stone-700">{evt.event}</span>
                    </div>
                  ))}
                </div>
              </div>
            )}
          </div>
        </div>
      )}

      {/* Query Bar */}
      <form onSubmit={handleSend} className="bg-white p-3 rounded-2xl border border-stone-200 shadow-xs flex items-center gap-3">
        <input
          type="text"
          placeholder="Ask Evidence Copilot specific questions about uploaded documents (e.g. 'What is the vibration limit?')..."
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          className="flex-1 bg-stone-50 border border-stone-200 rounded-xl px-4 py-2.5 text-xs text-stone-900 placeholder-stone-400 font-mono focus:outline-none focus:border-blue-600"
        />
        <button
          type="submit"
          disabled={loading}
          className="px-6 py-2.5 bg-blue-600 hover:bg-blue-700 text-white font-extrabold text-xs font-mono rounded-xl flex items-center gap-2 transition-all shadow-md disabled:opacity-50"
        >
          {loading ? "Querying AI Engine..." : "Send Query"}
          <Send className="w-3.5 h-3.5" />
        </button>
      </form>
    </div>
  );
}

