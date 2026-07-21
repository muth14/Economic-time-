const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000/api/v1";

export async function fetchAPI(endpoint: string, options: RequestInit = {}) {
  try {
    const res = await fetch(`${API_BASE_URL}${endpoint}`, {
      headers: {
        "Content-Type": "application/json",
        ...options.headers,
      },
      ...options,
    });
    if (!res.ok) {
      throw new Error(`HTTP error! status: ${res.status}`);
    }
    return await res.json();
  } catch (err) {
    console.warn(`API call to ${endpoint} failed, falling back to local client state:`, err);
    return null;
  }
}

export async function askCopilot(query: string, assetId?: string) {
  const data = await fetchAPI("/copilot/query", {
    method: "POST",
    body: JSON.stringify({ query, asset_id: assetId }),
  });
  return data;
}

export async function fetchKnowledgeGraph(query?: string) {
  const url = query ? `/graph/?query=${encodeURIComponent(query)}` : "/graph/";
  return await fetchAPI(url);
}

export async function fetchTimeTravelGraph(year: number) {
  return await fetchAPI(`/graph/time-travel?year=${year}`);
}

export async function fetchPlantRiskHeatmap() {
  return await fetchAPI("/predictive/heatmap");
}

export async function runWhatIfSimulation(entityId: string, failureMode: string) {
  return await fetchAPI("/predictive/what-if", {
    method: "POST",
    body: JSON.stringify({ trigger_entity_id: entityId, failure_mode: failureMode }),
  });
}

export async function generateSOP(assetId: string, procedureType: string) {
  return await fetchAPI("/predictive/sop", {
    method: "POST",
    body: JSON.stringify({ asset_id: assetId, procedure_type: procedureType }),
  });
}

export async function runAgentSwarm(prompt: string, targetAsset: string) {
  return await fetchAPI("/innovations/agent-swarm", {
    method: "POST",
    body: JSON.stringify({ prompt, target_asset: targetAsset }),
  });
}

export async function fetchEquipmentDNA(assetId: string) {
  return await fetchAPI(`/twin/dna/${assetId}`);
}

export async function submitIndustrialMemory(assetId: string, engineerName: string, correction: string, rootCause: string) {
  return await fetchAPI("/innovations/memory", {
    method: "POST",
    body: JSON.stringify({
      asset_id: assetId,
      engineer_name: engineerName,
      feedback_correction: correction,
      verified_root_cause: rootCause,
    }),
  });
}

export async function fetchCrossPlantIntelligence() {
  return await fetchAPI("/innovations/cross-plant");
}

export async function fetchPlantDoctorBriefing() {
  return await fetchAPI("/innovations/plant-doctor");
}

export async function fetchExecutiveDecision(assetId: string) {
  return await fetchAPI(`/innovations/executive-decision/${assetId}`);
}

export async function fetchExplainability(queryId: string) {
  return await fetchAPI(`/copilot/explainability/${queryId}`);
}

export async function uploadDocumentFile(file: File) {
  const formData = new FormData();
  formData.append("file", file);
  formData.append("file_type", file.name.split('.').pop()?.toUpperCase() || "PDF");

  try {
    const res = await fetch(`${API_BASE_URL}/documents/upload`, {
      method: "POST",
      body: formData,
    });
    if (!res.ok) throw new Error(`HTTP error ${res.status}`);
    return await res.json();
  } catch (err) {
    console.warn("Upload API failed, using fallback:", err);
    return null;
  }
}
