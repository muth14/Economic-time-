'use client';

import React, { createContext, useContext, useState } from 'react';
import { uploadDocumentFile } from '@/lib/api';

export const PIPELINE_STEPS = [
  "Upload Files",
  "OCR & Layout Parsing",
  "Spatial P&ID Symbol Detection",
  "Entity & Parameter Extraction",
  "Knowledge Graph Linkage",
  "Equipment DNA Profiling",
  "Vector Dense Embedding",
  "Hybrid Keyword Reranking",
  "Weibull Degradation Analysis",
  "Multi-Agent Swarm Consensus",
  "Analysis Complete"
];

interface WorkspaceContextType {
  isLoaded: boolean;
  isProcessing: boolean;
  processingStep: number;
  uploadedFiles: Array<{ name: string; size: string; type: string }>;
  extractedAssets: Array<any>;
  detectedEngineers: Array<any>;
  riskFindings: Array<any>;
  complianceIssues: Array<any>;
  loadGenChemDataset: () => void;
  uploadCustomFiles: (files: File[]) => void;
  resetWorkspace: () => void;
}

const WorkspaceContext = createContext<WorkspaceContextType | undefined>(undefined);

export function WorkspaceProvider({ children }: { children: React.ReactNode }) {
  const [isLoaded, setIsLoaded] = useState(false);
  const [isProcessing, setIsProcessing] = useState(false);
  const [processingStep, setProcessingStep] = useState(0);
  const [uploadedFiles, setUploadedFiles] = useState<Array<{ name: string; size: string; type: string }>>([]);
  const [extractedAssets, setExtractedAssets] = useState<Array<any>>([]);
  const [detectedEngineers, setDetectedEngineers] = useState<Array<any>>([]);
  const [riskFindings, setRiskFindings] = useState<Array<any>>([]);
  const [complianceIssues, setComplianceIssues] = useState<Array<any>>([]);

  const runPipelineAnimation = (onComplete: () => void) => {
    setIsProcessing(true);
    setProcessingStep(0);

    let step = 0;
    const interval = setInterval(() => {
      step += 1;
      if (step < PIPELINE_STEPS.length) {
        setProcessingStep(step);
      } else {
        clearInterval(interval);
        setIsProcessing(false);
        setIsLoaded(true);
        onComplete();
      }
    }, 400);
  };

  const loadGenChemDataset = () => {
    const genChemFiles = [
      { name: "Pump_P101_OEM_Manual.txt", size: "1.2 MB", type: "OEM Manual" },
      { name: "P101_Vibration_Anomaly_Incident_Report.txt", size: "850 KB", type: "Incident Report" },
      { name: "P_AND_ID_Boiler_Feed_System_Rev4.txt", size: "3.4 MB", type: "P&ID Schematic" },
      { name: "V101_Calibration_Certificate.txt", size: "420 KB", type: "Calibration" },
      { name: "P101_Telemetry_Log.csv", size: "27.3 MB", type: "Sensor Telemetry" },
      { name: "ISO_55001_Audit_Report.txt", size: "1.1 MB", type: "Audit Report" },
      { name: "Emergency_Seal_Flush_SOP.txt", size: "640 KB", type: "SOP" }
    ];
    setUploadedFiles(genChemFiles);

    runPipelineAnimation(() => {
      setExtractedAssets([
        { id: "P-101", name: "Boiler Feed Pump P-101", health: 64.5, risk: "Orange Warning", rul: 18, location: "Unit 4 Utility Bay" },
        { id: "V-101", name: "Steam Header Valve V-101", health: 78.0, risk: "Yellow", rul: 42, location: "Steam Line 2" },
        { id: "T-301", name: "Feedwater Storage Tank T-301", health: 92.4, risk: "Green Normal", rul: 110, location: "Tank Farm South" },
        { id: "C-201", name: "Hydrocracker Compressor C-201", health: 81.2, risk: "Green Normal", rul: 85, location: "Process Bay B" },
        { id: "M-102", name: "4160V Drive Motor M-102", health: 71.0, risk: "Yellow", rul: 35, location: "Unit 4 Utility Bay" }
      ]);
      setDetectedEngineers([
        { name: "Dr. Heinrich Weber", role: "Plant Manager" },
        { name: "Elena Rostova", role: "Lead Reliability Engineer" },
        { name: "Marcus Vance", role: "Senior Maintenance Engineer" },
        { name: "Ananya Sharma", role: "Control Room Operator" }
      ]);
      setRiskFindings([
        { asset: "P-101", severity: "High", title: "Drive-End Bearing Race Micro-Pitting", detail: "Vibration RMS peak 6.8 mm/s exceeding OEM 4.5 mm/s limit." },
        { asset: "V-101", severity: "Moderate", title: "Actuator Stem Packing Friction", detail: "Valve response lag 1.4s during automated closure testing." }
      ]);
      setComplianceIssues([
        { standard: "OISD-137", asset: "P-101", requirement: "Quarterly Mechanical Seal PM", status: "Overdue by 12 Days" },
        { standard: "PESO", asset: "T-301", requirement: "Safety Relief Valve Certification", status: "Expires in 14 Days" }
      ]);
    });
  };

  const uploadCustomFiles = async (files: File[]) => {
    const formatted = files.map(f => ({
      name: f.name,
      size: `${(f.size / (1024 * 1024)).toFixed(2)} MB`,
      type: f.name.split('.').pop()?.toUpperCase() || "Document"
    }));
    setUploadedFiles(prev => [...prev, ...formatted]);

    // Perform real API upload call
    const uploadResults = [];
    for (const f of files) {
      const res = await uploadDocumentFile(f);
      if (res && res.document) {
        uploadResults.push(res.document);
      }
    }

    runPipelineAnimation(() => {
      if (uploadResults.length > 0) {
        const allAssets: any[] = [];
        const allEngineers: any[] = [];
        const allRisks: any[] = [];
        const allCompliance: any[] = [];

        uploadResults.forEach(doc => {
          if (doc.extracted_assets) allAssets.push(...doc.extracted_assets);
          if (doc.detected_engineers) allEngineers.push(...doc.detected_engineers);
          if (doc.risk_findings) allRisks.push(...doc.risk_findings);
          if (doc.compliance_issues) allCompliance.push(...doc.compliance_issues);
        });

        setExtractedAssets(allAssets);
        setDetectedEngineers(allEngineers);
        setRiskFindings(allRisks);
        setComplianceIssues(allCompliance);
      } else {
        // Fallback for offline API mode
        setExtractedAssets([
          { id: "CUSTOM-01", name: `Parsed Asset (${files[0]?.name || 'Doc'})`, health: 75.0, risk: "Green Normal", rul: 60, location: "Local Document Stream" }
        ]);
        setDetectedEngineers([{ name: "Local Specialist", role: "Reliability Engineer" }]);
        setRiskFindings([]);
        setComplianceIssues([]);
      }
    });
  };

  const resetWorkspace = () => {
    setIsLoaded(false);
    setIsProcessing(false);
    setProcessingStep(0);
    setUploadedFiles([]);
    setExtractedAssets([]);
    setDetectedEngineers([]);
    setRiskFindings([]);
    setComplianceIssues([]);
  };

  return (
    <WorkspaceContext.Provider
      value={{
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
      }}
    >
      {children}
    </WorkspaceContext.Provider>
  );
}

export function useWorkspace() {
  const context = useContext(WorkspaceContext);
  if (!context) {
    throw new Error("useWorkspace must be used within a WorkspaceProvider");
  }
  return context;
}
