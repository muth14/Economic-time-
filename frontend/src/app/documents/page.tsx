'use client';

import React, { useState } from 'react';
import Link from 'next/link';
import { 
  FileText, 
  UploadCloud, 
  Search, 
  Tag, 
  Bot, 
  Layers
} from 'lucide-react';
import { useWorkspace } from '@/context/WorkspaceContext';

const sampleDocs = [
  {
    id: "DOC-101",
    filename: "Pump_P101_OEM_Manual.pdf",
    type: "OEM Manual",
    upload_time: "2026-06-01 10:30",
    page_count: 48,
    risk_level: "Low",
    summary: "Official Flowserve OEM Operating Manual for Boiler Feed Pump P-101 detailing vibration thresholds, seal flush plans (API Plan 53B), bearing temperature limits (<85°C), and preventive maintenance intervals.",
    entities: [
      { category: "Equipment Tag", value: "P-101" },
      { category: "Temperature Limit", value: "85 °C" },
      { category: "Pressure Limit", value: "140 bar" },
      { category: "Vendor", value: "Flowserve Corp" },
      { category: "Vibration Limit", value: "4.5 mm/s RMS" }
    ]
  },
  {
    id: "DOC-102",
    filename: "P101_Vibration_Anomaly_Incident_Report.pdf",
    type: "Incident Report",
    upload_time: "2026-07-12 14:15",
    page_count: 6,
    risk_level: "High",
    summary: "Root cause investigation into P-101 high drive-end bearing vibration (6.8 mm/s). The failure was attributed to mechanical seal leakage flushing lube oil out of the housing, resulting in micro-pitting on roller race.",
    entities: [
      { category: "Equipment Tag", value: "P-101" },
      { category: "Failure Code", value: "FAIL-BRG-2201" },
      { category: "Engineer", value: "Elena Rostova" },
      { category: "Maintenance Action", value: "Seal Replacement & Race Polishing" }
    ]
  },
  {
    id: "DOC-103",
    filename: "P_AND_ID_Boiler_Feed_System_Rev4.pdf",
    type: "P&ID Schematic",
    upload_time: "2026-07-01 09:00",
    page_count: 1,
    risk_level: "Medium",
    summary: "Piping & Instrumentation Diagram showing high-pressure boiler feed loop connecting Tank T-301 through Pump P-101 to Control Valve V-101 and Motor M-102 drive train.",
    entities: [
      { category: "Equipment Tag", value: "P-101" },
      { category: "Equipment Tag", value: "V-101" },
      { category: "Equipment Tag", value: "T-301" },
      { category: "Line Tag", value: "L-FEED-1004-900#" }
    ]
  }
];

export default function DocumentsPage() {
  const { isLoaded } = useWorkspace();
  const [selectedDoc, setSelectedDoc] = useState(sampleDocs[0]);
  const [search, setSearch] = useState('');

  if (!isLoaded) {
    return (
      <div className="max-w-4xl mx-auto py-16 text-center space-y-6 font-sans">
        <div className="w-16 h-16 rounded-2xl bg-blue-50 border border-blue-100 flex items-center justify-center mx-auto shadow-xs">
          <FileText className="w-8 h-8 text-blue-600" />
        </div>
        <h2 className="text-xl font-bold text-stone-900 font-sans">No Documents Uploaded Yet</h2>
        <p className="text-xs text-stone-600 max-w-md mx-auto font-sans">
          Please upload OEM Manuals, Incident Reports, or P&ID Schematics in the Workspace to activate Document Intelligence.
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

  return (
    <div className="space-y-6 max-w-6xl mx-auto font-sans pb-12">
      {/* Header */}
      <div className="flex flex-col md:flex-row md:items-center justify-between gap-4 border-b border-stone-200 pb-4">
        <div>
          <h1 className="text-2xl font-extrabold text-stone-900 flex items-center gap-2 font-sans">
            <FileText className="w-6 h-6 text-blue-600" /> Universal Document Intelligence
          </h1>
          <p className="text-xs text-stone-600 mt-1 font-sans">
            Auto-OCR, Entity Extraction & P&ID Drawing Parser (PDF, DOCX, CSV, Scanned Forms)
          </p>
        </div>

        <Link 
          href="/"
          className="px-4 py-2 bg-blue-600 hover:bg-blue-700 rounded-xl text-white font-bold text-xs font-mono flex items-center gap-2 shadow-sm transition-all"
        >
          <UploadCloud className="w-4 h-4" /> Upload Document / P&ID
        </Link>
      </div>

      {/* Main Grid */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6 font-sans">
        {/* Document List */}
        <div className="bg-white p-4 rounded-2xl border border-stone-200 space-y-3 shadow-xs">
          <div className="relative">
            <Search className="w-3.5 h-3.5 absolute left-3 top-1/2 -translate-y-1/2 text-stone-400" />
            <input
              type="text"
              placeholder="Search documents or extracted tags..."
              value={search}
              onChange={(e) => setSearch(e.target.value)}
              className="w-full bg-stone-50 border border-stone-200 rounded-lg pl-8 pr-3 py-1.5 text-xs text-stone-900 font-mono focus:outline-none focus:border-blue-600"
            />
          </div>

          <div className="space-y-2">
            {sampleDocs.map((doc) => {
              const isSelected = selectedDoc.id === doc.id;
              return (
                <div
                  key={doc.id}
                  onClick={() => setSelectedDoc(doc)}
                  className={`p-3 rounded-xl border cursor-pointer transition-all ${
                    isSelected
                      ? 'bg-blue-50 border-blue-200'
                      : 'bg-stone-50 border-stone-200 hover:border-stone-300'
                  }`}
                >
                  <div className="flex items-center justify-between text-xs mb-1 font-mono">
                    <span className="font-bold text-stone-900 truncate max-w-[170px]">{doc.filename}</span>
                    <span className="px-2 py-0.5 rounded text-[10px] font-bold bg-stone-200 text-stone-800">
                      {doc.risk_level} Risk
                    </span>
                  </div>
                  <div className="flex items-center justify-between text-[10px] text-stone-500 font-mono">
                    <span>{doc.type} • {doc.page_count} Pages</span>
                    <span>{doc.upload_time}</span>
                  </div>
                </div>
              );
            })}
          </div>
        </div>

        {/* Selected Document Inspection Panel */}
        <div className="lg:col-span-2 bg-white p-6 rounded-2xl border border-stone-200 space-y-6 shadow-xs">
          <div className="flex items-center justify-between border-b border-stone-200 pb-3">
            <div>
              <span className="text-[10px] bg-blue-50 text-blue-700 px-2 py-0.5 rounded border border-blue-200 font-mono font-bold">
                {selectedDoc.type}
              </span>
              <h2 className="text-lg font-bold text-stone-900 mt-1 font-sans">{selectedDoc.filename}</h2>
            </div>
            <Link
              href="/copilot"
              className="px-3 py-1.5 rounded-lg bg-blue-600 hover:bg-blue-700 text-white text-xs font-mono font-bold flex items-center gap-1.5 transition-all shadow-xs"
            >
              <Bot className="w-3.5 h-3.5" /> Ask AI on Document
            </Link>
          </div>

          {/* AI Extracted Summary */}
          <div>
            <h4 className="text-xs font-bold text-stone-500 uppercase tracking-wider mb-1 font-mono">AI Document Summary</h4>
            <p className="text-xs text-stone-700 bg-stone-50 p-3.5 rounded-xl border border-stone-200 leading-relaxed font-sans">
              {selectedDoc.summary}
            </p>
          </div>

          {/* Extracted Industrial Entities */}
          <div>
            <h4 className="text-xs font-bold text-stone-500 uppercase tracking-wider mb-2 flex items-center gap-1.5 font-mono">
              <Tag className="w-3.5 h-3.5 text-blue-600" /> Auto-Extracted Entities ({selectedDoc.entities.length})
            </h4>
            <div className="flex flex-wrap gap-2">
              {selectedDoc.entities.map((ent, idx) => (
                <div key={idx} className="flex items-center gap-1.5 px-3 py-1 rounded-lg bg-stone-50 border border-stone-200 text-xs font-mono">
                  <span className="text-stone-500 text-[10px]">{ent.category}:</span>
                  <span className="text-blue-600 font-bold">{ent.value}</span>
                </div>
              ))}
            </div>
          </div>

          {/* PDF Viewer Placeholder Canvas */}
          <div className="bg-[#FAFAF9] rounded-xl border border-stone-200 p-8 text-center space-y-3">
            <Layers className="w-10 h-10 text-blue-600 mx-auto opacity-80" />
            <p className="text-sm font-bold text-stone-900 font-sans">P&ID & Document Entity Highlighter View</p>
            <p className="text-xs text-stone-500 max-w-md mx-auto font-sans">
              Bounding boxes auto-highlighted for tags P-101, V-101, T-301, and API Plan 53B parameters.
            </p>
          </div>
        </div>
      </div>
    </div>
  );
}

