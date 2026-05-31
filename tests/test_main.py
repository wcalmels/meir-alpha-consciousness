"""
Tests for MEIR-α Consciousness Simulator
"""

import pytest
from meir_alpha_consciousness import MEIRAlphaConsciousness


@pytest.fixture
def system():
    """Create system instance for tests"""
    return MEIRAlphaConsciousness()


def test_initialization(system):
    """Test system initialization"""
    assert system.version == "1.0.0"
    assert system.status == "Proof of Concept"


def test_simulate_consciousness(system):
    """Test consciousness simulation"""
    result = system.simulate_consciousness({"test": "stimulus"})
    
    assert result["status"] == "success"
    assert result["project"] == "MEIR-α Consciousness Simulator"
    assert result["version"] == "1.0.0"


def test_info(system):
    """Test get_info function"""
    info = system.get_info()
    
    assert info["name"] == "MEIR-α Consciousness Simulator"
    assert info["version"] == "1.0.0"
    assert info["type"] == "research"


@pytest.mark.asyncio
async def test_async_simulate(system):
    """Test async consciousness simulation"""
    result = await system.simulate_consciousness_async({"test": "async"})
    assert result["status"] == "success"
