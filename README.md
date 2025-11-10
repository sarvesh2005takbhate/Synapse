# 🤖 Project Synapse - Agentic Last-Mile Coordinator

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://synapse-grabhack.streamlit.app/)
[![GitHub](https://img.shields.io/badge/GitHub-Repository-blue?logo=github)](https://github.com/aaravsingla/synapse)

Synapse is an AI-powered agent system designed to handle complex last-mile delivery and logistics scenarios. It acts as an intelligent coordinator that can analyze situations, make decisions, and execute actions while maintaining safety through policy-based confidence checks.

## 🌐 Live Demo
Try Synapse right now: **[https://synapse-grabhack.streamlit.app/](https://synapse-grabhack.streamlit.app/)**

No setup required - just visit the link and start experimenting with different logistics scenarios!




<img width="1817" height="808" alt="image" src="https://github.com/user-attachments/assets/2290f6c0-7621-40e9-bcb8-aaf17e9d3050" />



## 🎯 What Does Synapse Do?

Synapse handles challenging logistics scenarios such as:
- **Restaurant Overload**: Managing orders when restaurants have long prep times
- **Delivery Disputes**: Resolving damaged packaging conflicts between merchants and drivers
- **Recipient Unavailability**: Finding safe alternatives when recipients aren't available
- **Traffic Issues**: Rerouting rides and deliveries around obstacles
- **General Logistics**: Any custom scenario involving deliveries, rides, or customer service

<img width="919" height="714" alt="image" src="https://github.com/user-attachments/assets/b06d837b-66d5-419f-8d01-bec9ed682e74" />


## 🏗️ Architecture

The system follows a **THOUGHT → ACTION → OBSERVATION → POLICY** loop:

1. **THOUGHT**: Agent reasons about the situation
2. **ACTION**: Agent calls appropriate tools with JSON arguments
3. **OBSERVATION**: System executes the tool and returns results
4. **POLICY**: Safety system evaluates confidence and provides guidance
5. **Repeat** until a final plan is reached

## 🛠️ Available Tools

Synapse has access to **27 specialized tools**, grouped by function:

### 🚦 Traffic & Routing
- `check_traffic(origin, destination)` — Check traffic conditions.  
- `calculate_alternative_route(origin, destination)` — Find alternate routes.  
- `re_route_driver(driver_id, new_route)` — Reassign driver routes.  
- `assign_microtask(driver_id, task)` — Optimize driver idle time with micro-assignments.  

### 🛒 Merchant Management
- `get_merchant_status(merchant_id)` — Check restaurant prep times and status.  
- `get_nearby_merchants(merchant_type, location, radius_km)` — Find alternative merchants.  
- `log_merchant_packaging_feedback(merchant_id, feedback)` — Log quality issues.  
- `merchant_menu_equivalents(item, merchant_id)` — Suggest equivalent menu items across merchants.  

### 👥 Customer & Driver Communication
- `notify_customer(customer_id, message)` — Send customer notifications.  
- `notify_passenger_and_driver(passenger_id, driver_id, message)` — Notify both passenger and driver.  
- `contact_recipient_via_chat(recipient_id, message)` — Chat with recipients.  

### 📦 Delivery Management
- `find_nearby_locker(location)` — Locate secure parcel drop-off points.  
- `suggest_safe_drop_off(location)` — Recommend safe alternatives.  
- `verify_address(address_text)` — Validate and normalize delivery addresses.  
- `check_weather(location)` — Monitor weather for delivery impact.  

### ⚖️ Dispute Resolution
- `collect_evidence(order_id)` — Gather photos and documentation.  
- `analyze_evidence(evidence)` — AI analysis of dispute evidence.  
- `initiate_mediation_flow(order_id)` — Start formal mediation.  
- `issue_instant_refund(order_id, amount)` — Process refunds (**⚠️ capped at 20% of total order value**).  
- `exonerate_driver(driver_id)` — Clear driver of fault.  
- `notify_resolution(order_id, resolution)` — Communicate final resolution.  

### ✈️ Flight & Travel
- `check_flight_status(flight_number)` — Check flight delays for airport trips.  

### 🔒 Safety, Fraud & Compliance
- `voucher_policy_decider(context)` — Enforce voucher issuance policies.  
- `pii_redact(text)` — Redact personal identifiable information before use.  
- `policy_guard(action, args)` — Enforce allowlist/denylist and block unsafe actions.  
- `fraud_signal_check(order_id, customer_id)` — Detect fraud, abuse, or chargeback risk.  
- `resource_lock_manager(resource_id, action)` — Prevent double-assignments of resources.  
- `audit_log(entry)` — Append-only action log for accountability.  
- `metrics_emit(metric_name, value)` — Emit monitoring metrics for performance & safety.  



## 🚀 Getting Started

### Prerequisites
- Python 3.11+
- Google Gemini API key

### Installation

1. **Clone the repository**:
   ```bash
   git clone <your-repo-url>
   cd project-synapse
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your API key**:
   - Get a Gemini API key from Google AI Studio
   - For CLI usage: Set environment variable `GEMINI_API_KEY`
   - For Streamlit: Add to `.streamlit/secrets.toml`:
     ```toml
     GEMINI_API_KEY = "your-api-key-here"
     ```

## 🌐 Live Deployment
**Access the live app**: [https://synapse-grabhack.streamlit.app/](https://synapse-grabhack.streamlit.app/)

## 🖥️ Streamlit Frontend Features

The Streamlit web interface provides a professional, user-friendly experience:

### ✨ Key Features:
- **🎯 Pre-programmed Scenarios**: Choose from 4 professionally crafted scenarios:
  - Overloaded Restaurant Management
  - Damaged Packaging Dispute Resolution
  - Recipient Unavailable Handling
  - Traffic Obstruction Rerouting
- **✏️ Custom Issue Creation**: Input your own logistics scenarios and watch Synapse solve them
- **📊 Real-time Agent Visualization**: 
  - Step-by-step thought process display
  - Color-coded policy decisions (🟢 Safe / 🔴 Escalate)
  - JSON-formatted tool responses
  - Interactive trace following
- **🎨 Professional UI Design**: Clean, intuitive interface with organized sidebar controls
- **📱 Responsive Design**: Works on desktop, tablet, and mobile devices

### Usage Methods

#### 1. 🌐 Use the Live App (No Setup Required)
Visit: **[https://synapse-grabhack.streamlit.app/](https://synapse-grabhack.streamlit.app/)**

#### 2. 🖥️ Run Locally - Streamlit Interface
```bash
streamlit run app.py
```
- Full-featured web interface
- All scenarios and custom input available
- Real-time agent trace visualization

#### 2. Command Line Interface
```bash
python cli.py --scenario scenarios/overloaded_restaurant.json
```

#### 3. Python API
```python
from agents.agent_runner import run_scenario_text

result = run_scenario_text("Driver arrives but recipient is unavailable")
print(result["final_plan"])
```

## 📋 Built-in Scenarios

### 🍕 Overloaded Restaurant
**Challenge**: Restaurant has 40-minute prep time, customer expects 20 minutes
```json
{
  "id": "overloaded_rest_1",
  "description": "Order #A123: merchant m_22 reports prep_time_min=40, driver d_9 is idle nearby, customer c_55 expects food in 20 minutes. Resolve with minimal wait and minimal driver idle time."
}
```

### 📦 Damaged Packaging Dispute  
**Challenge**: Spilled drink dispute between driver and merchant
```json
{
  "id": "damaged_packaging_1", 
  "description": "Order #B789: At doorstep, customer reports spilled drink. Driver d_21 claims proper handover; merchant m_88 claims packaged correctly. Collect evidence, mediate, and resolve with minimal customer displeasure and clear driver status."
}
```

### 🏠 Recipient Unavailable
**Challenge**: Package delivery with no one home
```json
{
  "id": "recipient_unavailable_1",
  "description": "Order #C456: Delivery partner d_14 arrived, recipient r_300 not available. Package is valuable. Try to contact recipient, ask permission to leave, suggest safe drop-off or nearby locker if recipient declines."
}
```

### 🚗 Traffic Obstruction
**Challenge**: Airport trip with major traffic delays
```json
{
  "id": "traffic_obstruction_1",
  "description": "Ride R_900: Passenger p_66 is en route to airport. check_traffic shows a major accident with large delay. Recalculate alternate route, notify passenger and driver, and check flight status to provide context."
}
```

### ✏️ Custom Scenarios
Create your own scenarios directly in the web interface! Just select "Custom" and describe any logistics challenge you can think of.

## 🛡️ Safety & Policy System

Synapse includes a sophisticated policy system that:

- **Estimates Confidence**: Each tool execution gets a confidence score (0.0-1.0)
- **Escalation Logic**: Low confidence triggers conservative actions or human review
- **Suggested Actions**: Policy system can recommend next steps
- **Risk Mitigation**: Prevents high-risk actions when uncertain

### Policy Response Format
```json
{
  "confidence": 0.85,
  "escalate": false,
  "advice": "High confidence merchant fault. Proceed to refund customer.",
  "suggested_action": "issue_instant_refund",
  "suggested_args": {"order_id": "B789", "amount": 15.99}
}
```

## 🔧 Configuration

### Environment Variables
- `GEMINI_API_KEY` - Your Google Gemini API key
- `SYNAPSE_MODEL` - Model to use (default: `gemini-2.0-flash`)

### Model Options
- `gemini-2.0-flash` - Fast, good for development
- `gemini-2.5-flash` - More capable (if you have access)

## 📁 Project Structure

```
project-synapse/
├── agents/
│   ├── __init__.py
│   └── agent_runner.py      # Main agent logic
├── tools/
│   ├── __init__.py
│   ├── simulated_tools.py   # Tool implementations
│   └── policy.py            # Safety & confidence system
├── scenarios/               # Example scenarios
│   ├── damaged_packaging.json
│   ├── overloaded_restaurant.json
│   ├── recipient_unavailable.json
│   └── traffic_obstruction.json
├── logs/                    # Execution logs
├── .streamlit/
│   └── secrets.toml         # API keys
├── app.py                   # Streamlit web interface
├── cli.py                   # Command line interface
├── requirements.txt
└── README.md
```

## 🎮 How to Use Synapse

### 🌐 Web Interface (Recommended)
1. **Visit**: [https://synapse-grabhack.streamlit.app/](https://synapse-grabhack.streamlit.app/)
2. **Choose a scenario** from the sidebar or create your own custom scenario
3. **Click "Run Scenario"** and watch Synapse work through the problem
4. **Follow the agent's reasoning** with color-coded steps:
   - 🧠 **THOUGHT**: Agent's reasoning process
   - 🔧 **ACTION**: Tools being called with parameters
   - 📊 **OBSERVATION**: Results from tool execution
   - 🛡️ **POLICY**: Safety assessment and next steps
5. **Review the final plan** - A human-readable solution to the problem

### 💻 Local Development
1. **Clone and setup** (see Local Development Setup above)
2. **Run locally**: `streamlit run app.py`
3. **Develop custom tools** in `tools/simulated_tools.py`
4. **Create scenarios** in `scenarios/` directory
5. **Test via CLI**: `python cli.py --scenario your_scenario.json`

## 🌟 Professional Features

### 🏗️ Production-Ready Architecture
- **Modular Design**: Clean separation of agents, tools, and policies
- **Error Handling**: Graceful degradation and informative error messages  
- **Logging System**: Comprehensive execution traces saved to `logs/`
- **Configuration Management**: Environment-based settings
- **API Integration**: Google Gemini AI with proper client setup

### 🔒 Enterprise Safety Features
- **Confidence Scoring**: Every action gets a reliability score (0.0-1.0)
- **Escalation Logic**: Automatic human review triggers for uncertain situations
- **Policy Guidance**: AI-driven recommendations for safe next steps
- **Conservative Fallbacks**: Safe defaults when confidence is low

### 📊 Advanced Monitoring
- **Real-time Traces**: Watch every decision as it happens
- **JSON Logging**: Structured logs for analysis and debugging
- **Policy Visualization**: Clear indication of safety assessments
- **Performance Tracking**: Execution time and step counting

## 🔗 Links & Resources
- **🌐 Live Demo**: [https://synapse-grabhack.streamlit.app/](https://synapse-grabhack.streamlit.app/)
- **📁 GitHub Repository**: [https://github.com/aaravsingla/synapse](https://github.com/aaravsingla/synapse)
- **🤖 Google Gemini API**: [Get your API key](https://makersuite.google.com/app/apikey)
- **🚀 Streamlit Documentation**: [docs.streamlit.io](https://docs.streamlit.io)

## 🤝 Contributing & Development

This project demonstrates professional-grade AI agent development. Contributions welcome!

### 🛠️ Areas for Enhancement:
- **New Tools**: Add more logistics functions to `tools/simulated_tools.py`
- **Scenarios**: Create domain-specific scenarios in `scenarios/`
- **Policy Rules**: Enhance safety logic in `tools/policy.py`
- **UI Improvements**: Upgrade the Streamlit interface in `app.py`
- **Integration**: Connect to real APIs instead of simulated tools

### 📈 Architecture Patterns Demonstrated:
- **Agent-Tool Architecture**: Clean separation of reasoning and execution
- **Policy-Based Safety**: Confidence scoring and escalation logic
- **Modular Design**: Easy to extend and maintain
- **Production Deployment**: Ready for cloud platforms like Streamlit Cloud

---

**⚡ Ready to see AI agents in action?** 
**👉 Try the live demo: [https://synapse-grabhack.streamlit.app/](https://synapse-grabhack.streamlit.app/)**

*Synapse demonstrates how AI agents can handle complex, multi-step logistics problems while maintaining safety through policy-based decision making - perfect for learning advanced AI development patterns.*




