'use client';

import React, { useState } from 'react';
import Link from 'next/link';
import { 
  Boxes, 
  Activity, 
  MessageSquare, 
  Wrench, 
  FileText, 
  Sliders, 
  Zap, 
  Send,
  Cpu,
  Dna
} from 'lucide-react';
import { useWorkspace } from '@/context/WorkspaceContext';

const sampleAssets = [
  {
    id: "P-101",
    name: "Centrifugal Boiler Feed Pump P-101",
    type: "Pump",
    location: "Unit 4 - Power & Utility Bay",
    status: "Warning",
    health: 64.5,
    rul_days: 18,
    telemetry: { "Vibration": "6.8 mm/s", "Bearing Temp": "78.4 °C", "Discharge Pressure": "118 bar", "Motor Current": "410 A" },
    specifications: { "Flow Rate": "450 m³/h", "Head": "120 bar", "Manufacturer": "Flowserve Corp", "Serial": "FS-2021-99841" }
  },
  {
    id: "V-101",
    name: "Main Steam Pressure Control Valve V-101",
    type: "Valve",
    location: "Unit 4 - Steam Header Line 2",
    status: "Critical",
    health: 42.0,
    rul_days: 6,
    telemetry: { "Position Feedback": "48%", "Actuator Air": "3.1 bar", "Upstream Pressure": "88 bar", "Friction Index": "High" },
    specifications: { "Valve Size": "12 Inch", "Rating": "ANSI Class 900", "Actuator": "Pneumatic Diaphragm", "Manufacturer": "Fisher Emerson" }
  },
  {
    id: "C-201",
    name: "Heavy Duty Hydrogen Gas Compressor C-201",
    type: "Compressor",
    location: "Hydrocracker Unit B",
    status: "Normal",
    health: 92.0,
    rul_days: 145,
    telemetry: { "Suction Temp": "34 °C", "Discharge Temp": "142 °C", "Lube Pressure": "5.4 bar", "RPM": "1480" },
    specifications: { "Capacity": "12,000 Nm³/h", "Driver": "6kV 1.2MW", "Manufacturer": "Siemens Energy" }
  }
];

export default function DigitalTwinPage() {
  const { isLoaded, extractedAssets } = useWorkspace();

  const activeAssets = extractedAssets.length > 0 ? extractedAssets.map(a => ({
    id: a.id,
    name: a.name || `Asset ${a.id}`,
    type: a.id.split('-')[0] || "Equipment",
    location: a.location || "Uploaded Unit Bay",
    status: a.health < 70 ? "Warning" : "Normal",
    health: a.health || 85.0,
    rul_days: a.rul || 45,
    telemetry: { "Vibration": "6.8 mm/s", "Bearing Temp": "78.4 °C", "Discharge Pressure": "118 bar", "Status": a.risk || "Normal" },
    specifications: { "Manufacturer": "Extracted Vendor", "Serial": `SN-GEN-${a.id}`, "Line": "Primary Fluid Loop" }
  })) : sampleAssets;

  const [selectedAsset, setSelectedAsset] = useState(activeAssets[0]);
  const [chatMessage, setChatMessage] = useState('');
  const [chatHistory, setChatHistory] = useState([
    { sender: activeAssets[0].id, text: `Hello! I am ${activeAssets[0].name}. My current health score is ${activeAssets[0].health}%. How can I help you today?` }
  ]);

  if (!isLoaded) {
    return (
      <div className="max-w-4xl mx-auto py-16 text-center space-y-6 font-sans">
        <div className="w-16 h-16 rounded-2xl bg-[#FFF7ED] border border-[#FFEDD5] flex items-center justify-center mx-auto shadow-xs">
          <Dna className="w-8 h-8 text-[#F9572A]" />
        </div>
        <h2 className="text-xl font-bold text-stone-900 font-sans">No Equipment DNA Data Available Yet</h2>
        <p className="text-xs text-stone-600 max-w-md mx-auto font-sans">
          Please upload industrial schematics or telemetry logs in the Workspace to generate Equipment DNA profiles.
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

  const handleChatSend = (e: React.FormEvent) => {
    e.preventDefault();
    if (!chatMessage.trim()) return;

    const userText = chatMessage;
    setChatHistory(prev => [...prev, { sender: 'User', text: userText }]);
    setChatMessage('');

    setTimeout(() => {
      let reply = `As ${selectedAsset.id}, my health score is ${selectedAsset.health}%. My current operating pressure is 118 bar. All telemetry parameters are synced to the Cerebras Knowledge Graph.`;
      if (userText.toLowerCase().includes("seal") || userText.toLowerCase().includes("fail")) {
        reply = `My drive-end bearing seal flush plan (API Plan 53B) experienced a pressure drop on July 12th. I recommend checking my nitrogen bladder pressure.`;
      }
      setChatHistory(prev => [...prev, { sender: selectedAsset.id, text: reply }]);
    }, 600);
  };

  return (
    <div className="space-y-6 max-w-6xl mx-auto font-sans pb-12">
      {/* Header */}
      <div className="flex flex-col md:flex-row md:items-center justify-between gap-4 border-b border-stone-200 pb-4">
        <div>
          <h1 className="text-2xl font-extrabold text-stone-900 flex items-center gap-2 font-sans">
            <Boxes className="w-6 h-6 text-[#F9572A]" /> Asset Digital Twin & Machine Chat
          </h1>
          <p className="text-xs text-stone-600 mt-1 font-sans">
            Physical Asset Telemetry, Connected Graph Topology, and Innovation Machine Chatbot
          </p>
        </div>

        {/* Asset Switcher */}
        <div className="flex items-center gap-2">
          {activeAssets.map(a => (
            <button
              key={a.id}
              onClick={() => setSelectedAsset(a)}
              className={`px-3 py-1.5 rounded-lg text-xs font-bold font-mono transition-all border ${
                selectedAsset.id === a.id
                  ? 'bg-[#FFF7ED] text-[#F9572A] border-[#FFEDD5] shadow-xs'
                  : 'bg-white text-stone-600 border-stone-200 hover:text-stone-900'
              }`}
            >
              {a.id}
            </button>
          ))}
        </div>
      </div>

      {/* Main Digital Twin Grid */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6 font-sans">
        {/* Left Column: Asset Card & Telemetry Stream */}
        <div className="space-y-6">
          <div className="bg-white p-5 rounded-2xl border border-stone-200 space-y-4 shadow-xs">
            <div className="flex items-center justify-between">
              <span className="text-[10px] bg-stone-100 text-stone-700 px-2 py-0.5 rounded border border-stone-200 font-mono font-bold">
                {selectedAsset.type} Twin
              </span>
              <span className="px-2 py-0.5 rounded text-[10px] font-mono font-bold bg-[#FFF7ED] text-[#F9572A] border border-[#FFEDD5]">
                {selectedAsset.status}
              </span>
            </div>

            <div>
              <div className="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded bg-stone-100 border border-stone-200 text-stone-800 text-[10px] font-mono mb-1 font-bold">
                <Dna className="w-3 h-3 text-[#F9572A]" /> DNA: DNA-HYD-99841-{selectedAsset.id}
              </div>
              <h2 className="text-base font-bold text-stone-900">{selectedAsset.name}</h2>
              <p className="text-xs text-stone-500 font-mono mt-0.5">{selectedAsset.location}</p>
            </div>

            {/* Health Meter */}
            <div className="space-y-1">
              <div className="flex justify-between text-xs font-mono">
                <span className="text-stone-500">Health Index:</span>
                <span className="font-bold text-[#F9572A]">{selectedAsset.health}%</span>
              </div>
              <div className="w-full h-2 bg-stone-100 rounded-full overflow-hidden border border-stone-200">
                <div className="h-full bg-[#F9572A] rounded-full" style={{ width: `${selectedAsset.health}%` }} />
              </div>
            </div>

            {/* Telemetry Stream Grid */}
            <div>
              <h4 className="text-xs font-bold text-stone-700 uppercase tracking-wider mb-2 flex items-center gap-1.5 font-mono">
                <Activity className="w-3.5 h-3.5 text-[#F9572A]" /> Live Sensor Telemetry
              </h4>
              <div className="grid grid-cols-2 gap-2">
                {Object.entries(selectedAsset.telemetry).map(([k, v]) => (
                  <div key={k} className="p-2.5 rounded-lg bg-[#FAFAF9] border border-stone-200 font-mono">
                    <span className="text-[10px] text-stone-500 block">{k}</span>
                    <span className="text-xs font-bold text-stone-900">{v}</span>
                  </div>
                ))}
              </div>
            </div>
          </div>
        </div>

        {/* Right Column: Machine Chatbot */}
        <div className="lg:col-span-2 bg-white p-5 rounded-2xl border border-stone-200 flex flex-col justify-between min-h-[480px] shadow-xs">
          <div>
            <div className="flex items-center justify-between border-b border-stone-200 pb-3 mb-4">
              <div className="flex items-center gap-2">
                <div className="w-8 h-8 rounded-xl bg-[#FFF7ED] border border-[#FFEDD5] flex items-center justify-center">
                  <MessageSquare className="w-4 h-4 text-[#F9572A]" />
                </div>
                <div>
                  <h3 className="text-sm font-bold text-stone-900">Equipment Machine AI</h3>
                  <p className="text-[11px] text-stone-500 font-mono">Interactive Agent for {selectedAsset.id}</p>
                </div>
              </div>
              <span className="text-xs text-emerald-700 font-mono font-bold flex items-center gap-1">
                <span className="w-2 h-2 rounded-full bg-emerald-500 animate-pulse" /> Telemetry Online
              </span>
            </div>

            {/* Chat Stream */}
            <div className="space-y-3 max-h-[320px] overflow-y-auto pr-2 font-mono text-xs">
              {chatHistory.map((msg, idx) => {
                const isUser = msg.sender === 'User';
                return (
                  <div key={idx} className={`flex ${isUser ? 'justify-end' : 'justify-start'}`}>
                    <div className={`p-3 rounded-2xl max-w-md leading-relaxed ${
                      isUser
                        ? 'bg-[#F9572A] text-white rounded-br-none font-sans font-semibold'
                        : 'bg-[#FAFAF9] border border-stone-200 text-stone-800 rounded-bl-none'
                    }`}>
                      <div className="font-bold text-[10px] mb-1 font-mono">{msg.sender}</div>
                      <p>{msg.text}</p>
                    </div>
                  </div>
                );
              })}
            </div>
          </div>

          {/* Chat Form */}
          <form onSubmit={handleChatSend} className="mt-4 flex items-center gap-2 pt-3 border-t border-stone-200">
            <input
              type="text"
              placeholder={`Ask ${selectedAsset.id} a direct question (e.g. 'What is your bearing temp?')`}
              value={chatMessage}
              onChange={(e) => setChatMessage(e.target.value)}
              className="flex-1 bg-stone-50 border border-stone-200 rounded-xl px-4 py-2 text-xs text-stone-900 font-mono focus:outline-none focus:border-[#F9572A]"
            />
            <button
              type="submit"
              className="px-4 py-2 bg-[#F9572A] hover:bg-[#EA580C] text-white font-bold text-xs font-mono rounded-xl flex items-center gap-1.5 transition-all shadow-sm"
            >
              Send <Send className="w-3.5 h-3.5" />
            </button>
          </form>
        </div>
      </div>
    </div>
  );
}
