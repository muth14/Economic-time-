'use client';

import React, { useState, useEffect } from 'react';
import { 
  Network, 
  Search, 
  Clock, 
  Filter, 
  Boxes, 
  FileText, 
  User, 
  Info, 
  Maximize2, 
  Sparkles,
  GitBranch
} from 'lucide-react';
import { fetchKnowledgeGraph, fetchTimeTravelGraph } from '@/lib/api';
import { KnowledgeGraphData, GraphNode } from '@/lib/types';

export default function GraphExplorerPage() {
  const [graphData, setGraphData] = useState<KnowledgeGraphData | null>(null);
  const [selectedYear, setSelectedYear] = useState<number>(2026);
  const [searchQuery, setSearchQuery] = useState('');
  const [selectedNode, setSelectedNode] = useState<GraphNode | null>(null);
  const [diffSummary, setDiffSummary] = useState('');

  useEffect(() => {
    loadGraph();
  }, [selectedYear]);

  const loadGraph = async () => {
    const res = await fetchTimeTravelGraph(selectedYear);
    if (res && res.graph) {
      setGraphData(res.graph);
      setDiffSummary(res.diff_summary);
      if (res.graph.nodes.length > 0) {
        setSelectedNode(res.graph.nodes[0]);
      }
    }
  };

  const handleSearch = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!searchQuery.trim()) {
      loadGraph();
      return;
    }
    const res = await fetchKnowledgeGraph(searchQuery);
    if (res) {
      setGraphData(res);
      if (res.nodes.length > 0) {
        setSelectedNode(res.nodes[0]);
      }
    }
  };

  return (
    <div className="space-y-6 max-w-7xl mx-auto">
      {/* Top Header */}
      <div className="flex flex-col md:flex-row md:items-center justify-between gap-4 border-b border-slate-800 pb-4">
        <div>
          <h1 className="text-2xl font-extrabold text-white flex items-center gap-2">
            <Network className="w-6 h-6 text-purple-400" /> Enterprise Knowledge Graph & Time Travel
          </h1>
          <p className="text-xs text-slate-400 mt-0.5">
            Interactive Neo4j Graph Visualizer with Temporal Timeline Evolution (2021 - 2026)
          </p>
        </div>

        {/* Natural Language Search */}
        <form onSubmit={handleSearch} className="flex items-center gap-2">
          <div className="relative">
            <Search className="w-4 h-4 absolute left-3 top-1/2 -translate-y-1/2 text-slate-400" />
            <input
              type="text"
              placeholder="Filter graph by entity (e.g. Pump, Elena, Seal)"
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              className="bg-slate-900 border border-slate-700 rounded-lg pl-9 pr-4 py-1.5 text-xs text-slate-200 focus:outline-none focus:border-purple-500 w-64"
            />
          </div>
          <button type="submit" className="px-3 py-1.5 bg-purple-600 hover:bg-purple-500 text-white text-xs rounded-lg font-semibold transition-all">
            Filter Graph
          </button>
        </form>
      </div>

      {/* Time Travel Slider Control */}
      <div className="glass-panel p-4 rounded-xl border border-purple-500/30 bg-purple-950/20">
        <div className="flex items-center justify-between mb-2">
          <span className="text-xs font-bold text-purple-300 flex items-center gap-1.5 font-mono">
            <Clock className="w-4 h-4 text-purple-400" /> GRAPH TIME TRAVEL TIMELINE
          </span>
          <span className="text-xs font-mono font-bold bg-purple-900 px-3 py-1 rounded text-purple-200 border border-purple-700">
            Year {selectedYear} Topology
          </span>
        </div>

        <input
          type="range"
          min="2021"
          max="2026"
          step="1"
          value={selectedYear}
          onChange={(e) => setSelectedYear(parseInt(e.target.value))}
          className="w-full accent-purple-500 cursor-pointer"
        />

        <div className="flex justify-between text-[10px] font-mono text-slate-400 mt-1">
          <span>2021 (Commissioning)</span>
          <span>2023 (Valve V-101)</span>
          <span>2026 (Live Triples)</span>
        </div>

        {diffSummary && (
          <p className="text-xs text-purple-300 font-mono mt-2 pt-2 border-t border-purple-900/60">
            ⚡ <strong>Snapshot Summary:</strong> {diffSummary}
          </p>
        )}
      </div>

      {/* Main Graph Grid */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        {/* Canvas Visualizer Panel */}
        <div className="lg:col-span-2 glass-panel p-4 rounded-2xl border border-slate-700/60 min-h-[480px] relative flex flex-col justify-between overflow-hidden">
          <div className="flex items-center justify-between text-xs text-slate-400 mb-2">
            <div className="flex items-center gap-4">
              <span className="flex items-center gap-1.5"><span className="w-2.5 h-2.5 rounded-full bg-cyan-400" /> Equipment</span>
              <span className="flex items-center gap-1.5"><span className="w-2.5 h-2.5 rounded-full bg-amber-400" /> Incident</span>
              <span className="flex items-center gap-1.5"><span className="w-2.5 h-2.5 rounded-full bg-purple-400" /> Engineer</span>
              <span className="flex items-center gap-1.5"><span className="w-2.5 h-2.5 rounded-full bg-emerald-400" /> Regulation</span>
            </div>
            <span className="font-mono">{graphData?.nodes.length || 0} Nodes • {graphData?.edges.length || 0} Edges</span>
          </div>

          {/* Force Graph Interactive Layout */}
          <div className="flex-1 w-full bg-slate-950/80 rounded-xl border border-slate-800/80 p-6 relative flex items-center justify-center overflow-auto">
            <svg className="absolute inset-0 w-full h-full pointer-events-none">
              {graphData?.edges.map((edge, idx) => {
                // Calculate position offsets for demo layout
                const sourceIdx = graphData.nodes.findIndex(n => n.id === edge.source);
                const targetIdx = graphData.nodes.findIndex(n => n.id === edge.target);
                const sx = 100 + (sourceIdx % 4) * 160;
                const sy = 100 + Math.floor(sourceIdx / 4) * 120;
                const tx = 100 + (targetIdx % 4) * 160;
                const ty = 100 + Math.floor(targetIdx / 4) * 120;

                return (
                  <g key={idx}>
                    <line x1={sx} y1={sy} x2={tx} y2={ty} stroke="#334155" strokeWidth="1.5" strokeDasharray="4" />
                    <text x={(sx + tx) / 2} y={(sy + ty) / 2} fill="#64748b" fontSize="9" textAnchor="middle" dy="-4">
                      {edge.type}
                    </text>
                  </g>
                );
              })}
            </svg>

            {/* Nodes */}
            <div className="grid grid-cols-2 md:grid-cols-4 gap-8 relative z-10 w-full">
              {graphData?.nodes.map((node) => {
                const isSelected = selectedNode?.id === node.id;
                let colorClass = "from-cyan-500 to-blue-600 border-cyan-400";
                if (node.type === "Engineer") colorClass = "from-purple-500 to-indigo-600 border-purple-400";
                if (node.type === "Incident" || node.type === "Failure") colorClass = "from-amber-500 to-rose-600 border-amber-400";
                if (node.type === "Regulation" || node.type === "SafetyProcedure") colorClass = "from-emerald-500 to-teal-600 border-emerald-400";

                return (
                  <button
                    key={node.id}
                    onClick={() => setSelectedNode(node)}
                    className={`p-3 rounded-xl bg-gradient-to-tr ${colorClass} text-white font-medium text-xs shadow-lg transition-all transform hover:scale-105 border ${
                      isSelected ? 'ring-4 ring-cyan-400 shadow-cyan-500/50 scale-105' : 'opacity-90 hover:opacity-100'
                    }`}
                  >
                    <div className="font-bold font-mono text-[11px] uppercase tracking-wider">{node.id}</div>
                    <div className="text-[10px] text-slate-100 truncate">{node.label}</div>
                    <div className="text-[9px] bg-slate-900/60 px-1.5 py-0.5 rounded mt-1 inline-block font-mono">
                      {node.type}
                    </div>
                  </button>
                );
              })}
            </div>
          </div>
        </div>

        {/* Selected Node Inspector */}
        <div className="glass-panel p-5 rounded-2xl border border-slate-700/60 space-y-4">
          <h3 className="text-sm font-bold text-white flex items-center gap-2 border-b border-slate-800 pb-2">
            <Info className="w-4 h-4 text-cyan-400" /> Knowledge Node Inspector
          </h3>

          {selectedNode ? (
            <div className="space-y-4 text-xs">
              <div>
                <span className="text-[10px] text-slate-500 uppercase tracking-widest font-mono">Node Identifier</span>
                <p className="text-base font-extrabold text-cyan-400 font-mono">{selectedNode.id}</p>
                <p className="text-xs text-slate-200 font-medium">{selectedNode.label}</p>
              </div>

              <div>
                <span className="text-[10px] text-slate-500 uppercase tracking-widest font-mono">Entity Type</span>
                <p className="text-xs text-purple-400 font-bold">{selectedNode.type}</p>
              </div>

              {selectedNode.attributes && (
                <div>
                  <span className="text-[10px] text-slate-500 uppercase tracking-widest font-mono">Attributes & Metadata</span>
                  <div className="bg-slate-900 p-3 rounded-lg border border-slate-800 space-y-1 mt-1 font-mono text-[11px]">
                    {Object.entries(selectedNode.attributes).map(([k, v]) => (
                      <div key={k} className="flex justify-between">
                        <span className="text-slate-400">{k}:</span>
                        <span className="text-slate-200 font-bold">{String(v)}</span>
                      </div>
                    ))}
                  </div>
                </div>
              )}

              <div>
                <span className="text-[10px] text-slate-500 uppercase tracking-widest font-mono">Connected Graph Relationships</span>
                <div className="space-y-1.5 mt-1">
                  {graphData?.edges
                    .filter(e => e.source === selectedNode.id || e.target === selectedNode.id)
                    .map((edge, idx) => (
                      <div key={idx} className="p-2 rounded bg-slate-900 border border-slate-800 text-[11px] flex items-center justify-between">
                        <span className="text-slate-300 font-mono">{edge.source === selectedNode.id ? `→ ${edge.target}` : `← ${edge.source}`}</span>
                        <span className="text-cyan-400 font-bold font-mono text-[10px]">{edge.type}</span>
                      </div>
                    ))}
                </div>
              </div>
            </div>
          ) : (
            <p className="text-xs text-slate-500 italic">Select any node on the graph canvas to inspect properties.</p>
          )}
        </div>
      </div>
    </div>
  );
}
