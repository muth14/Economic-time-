from app.services.predictive_engine import predictive_service

def test_weibull_failure_probability():
    prob_0 = predictive_service.calculate_weibull_failure_probability(0)
    prob_365 = predictive_service.calculate_weibull_failure_probability(365)
    assert prob_0 == 0.0
    assert prob_365 > 0.5

def test_rul_days_estimation():
    rul_high = predictive_service.calculate_rul_days(vibration_rms=2.5)
    rul_low = predictive_service.calculate_rul_days(vibration_rms=7.5)
    assert rul_high > rul_low

def test_what_if_cascade_simulation():
    what_if = predictive_service.simulate_what_if_failure("V-101", "Diaphragm Rupture")
    assert what_if.trigger_entity == "V-101"
    assert len(what_if.cascade_chain) >= 2
    assert what_if.total_plant_downtime_est_hours > 0
    assert what_if.est_financial_loss_usd > 0
