import streamlit as st
from datetime import date, datetime

st.set_page_config(
    page_title="গ্যারেজ ও চার্জিং স্টেশন ব্যবস্থাপনা",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- প্রফেশনাল Apple Liquid Glass & Hind Siliguri ফন্ট CSS ---
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Hind+Siliguri:wght@400;500;600;700&display=swap');

    html, body, [class*="css"], .stMarkdown, button, input, select, div {
        font-family: 'Hind Siliguri', -apple-system, BlinkMacSystemFont, sans-serif !important;
    }

    /* Streamlit-এর অপ্রয়োজনীয় Deploy বার ও ফুটার হাইড করা */
    #MainMenu, footer, .stDeployButton {
        display: none !important;
    }
    header[data-testid="stHeader"] {
        background: transparent !important;
    }

    /* মূল ব্যাকগ্রাউন্ড: macOS সিলভার-ব্লু লিকুইড ব্যাকগ্রাউন্ড */
    .stApp {
        background: 
            radial-gradient(at 0% 0%, rgba(186, 224, 255, 0.78) 0px, transparent 50%),
            radial-gradient(at 100% 0%, rgba(224, 206, 255, 0.68) 0px, transparent 50%),
            radial-gradient(at 100% 100%, rgba(196, 240, 232, 0.68) 0px, transparent 50%),
            radial-gradient(at 0% 100%, rgba(215, 228, 255, 0.72) 0px, transparent 50%),
            #eef2f8 !important;
        background-attachment: fixed !important;
    }

    /* =================================================================
       বাম পাশের সাইডবার: প্রিমিয়াম Apple Liquid Glass নেভিগেশন মেনু
       ================================================================= */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, rgba(255, 255, 255, 0.62) 0%, rgba(238, 244, 255, 0.52) 100%) !important;
        backdrop-filter: blur(32px) saturate(210%) !important;
        -webkit-backdrop-filter: blur(32px) saturate(210%) !important;
        border-right: 1.5px solid rgba(255, 255, 255, 0.9) !important;
        box-shadow: 8px 0 30px rgba(15, 23, 42, 0.06) !important;
    }
    section[data-testid="stSidebar"] > div:first-child {
        padding-top: 1.4rem !important;
        padding-left: 1rem !important;
        padding-right: 1rem !important;
    }

    /* সাইডবার ব্র্যান্ড ও মেনু হেডার কার্ড */
    .sidebar-brand-box {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.85) 0%, rgba(235, 245, 255, 0.7) 100%);
        border: 1.5px solid rgba(255, 255, 255, 0.98);
        border-radius: 18px;
        padding: 14px 16px;
        margin-bottom: 18px;
        text-align: center;
        box-shadow: 0 8px 22px rgba(0, 102, 255, 0.08), inset 0 1px 1px rgba(255, 255, 255, 1);
    }
    .sidebar-brand-title {
        font-size: 20px;
        font-weight: 700;
        color: #0f172a;
        letter-spacing: 0.3px;
        margin: 0;
    }
    .sidebar-brand-sub {
        font-size: 12px;
        font-weight: 600;
        color: #0066ff;
        margin-top: 2px;
    }

    /* সাইডবারের প্রতিটি মেনু বাটন */
    section[data-testid="stSidebar"] .stButton > button {
        width: 100% !important;
        height: 48px !important;
        border-radius: 15px !important;
        padding: 0 16px !important;
        margin-bottom: 4px !important;
        display: flex !important;
        align-items: center !important;
        justify-content: flex-start !important;
        text-align: left !important;
        transition: all 0.22s cubic-bezier(0.25, 0.8, 0.25, 1) !important;
    }
    section[data-testid="stSidebar"] .stButton > button p {
        font-size: 16px !important;
        font-weight: 600 !important;
        letter-spacing: 0.2px !important;
    }
    section[data-testid="stSidebar"] .stButton > button[kind="secondary"] {
        background: rgba(255, 255, 255, 0.52) !important;
        border: 1.5px solid rgba(255, 255, 255, 0.88) !important;
        color: #334155 !important;
        box-shadow: 0 4px 12px rgba(15, 23, 42, 0.03), inset 0 1px 1px rgba(255, 255, 255, 0.95) !important;
    }
    section[data-testid="stSidebar"] .stButton > button[kind="secondary"]:hover {
        background: rgba(255, 255, 255, 0.92) !important;
        border-color: rgba(0, 102, 255, 0.45) !important;
        color: #0066ff !important;
        transform: translateX(4px) !important;
        box-shadow: 0 6px 18px rgba(0, 102, 255, 0.12) !important;
    }
    section[data-testid="stSidebar"] .stButton > button[kind="primary"] {
        background: linear-gradient(135deg, #0a84ff 0%, #0066ff 100%) !important;
        border: 1.5px solid rgba(255, 255, 255, 0.65) !important;
        color: #ffffff !important;
        box-shadow: 0 8px 20px rgba(0, 102, 255, 0.28), inset 0 1px 1px rgba(255, 255, 255, 0.45) !important;
        transform: translateX(3px) !important;
    }
    section[data-testid="stSidebar"] .stButton > button[kind="primary"] p {
        color: #ffffff !important;
        font-weight: 700 !important;
    }

    /* মূল কনটেন্ট এরিয়া মার্জিন ও প্রস্থ নিয়ন্ত্রণ */
    .block-container {
        max-width: 1340px !important;
        padding-top: 1.4rem !important;
        padding-bottom: 3rem !important;
        padding-left: 1.2rem !important;
        padding-right: 1.2rem !important;
    }

    /* কাস্টম প্রফেশনাল টপ অ্যাপ-বার */
    .pro-header {
        background: rgba(255, 255, 255, 0.48);
        backdrop-filter: blur(28px) saturate(200%);
        -webkit-backdrop-filter: blur(28px) saturate(200%);
        border: 1.5px solid rgba(255, 255, 255, 0.85);
        border-radius: 22px;
        padding: 18px 26px;
        margin-bottom: 20px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        box-shadow: 0 10px 28px rgba(20, 35, 70, 0.06), inset 0 1px 1px rgba(255, 255, 255, 0.95);
    }
    .pro-title {
        font-size: 26px;
        font-weight: 700;
        color: #0f172a;
        margin: 0;
        line-height: 1.25;
    }
    .pro-subtitle {
        font-size: 14px;
        font-weight: 500;
        color: #475569;
        margin-top: 3px;
    }
    .due-pill-zero {
        background: rgba(16, 185, 129, 0.14);
        border: 1px solid rgba(16, 185, 129, 0.35);
        color: #065f46;
        padding: 9px 18px;
        border-radius: 999px;
        font-weight: 700;
        font-size: 15px;
    }
    .due-pill-active {
        background: rgba(239, 68, 68, 0.14);
        border: 1px solid rgba(239, 68, 68, 0.35);
        color: #991b1b;
        padding: 9px 18px;
        border-radius: 999px;
        font-weight: 700;
        font-size: 15px;
    }

    /* লিকুইড গ্লাস কার্ড কন্টেইনার */
    div[data-testid="stVerticalBlockBorderWrapper"] {
        background: rgba(255, 255, 255, 0.52) !important;
        backdrop-filter: blur(26px) saturate(195%) !important;
        -webkit-backdrop-filter: blur(26px) saturate(195%) !important;
        border: 1.5px solid rgba(255, 255, 255, 0.88) !important;
        border-radius: 20px !important;
        box-shadow: 0 8px 24px rgba(15, 23, 42, 0.045), inset 0 1px 1px rgba(255, 255, 255, 0.95) !important;
        padding: 12px 16px !important;
        margin-bottom: 12px !important;
    }

    .step-mini-label {
        font-size: 11.5px;
        font-weight: 700;
        color: #64748b;
        margin-bottom: 4px;
        letter-spacing: 0.2px;
    }
    .extra-hour-pill {
        background: rgba(255, 255, 255, 0.65);
        border: 1.5px solid rgba(255, 255, 255, 0.9);
        border-radius: 12px;
        padding: 7px 4px;
        text-align: center;
        font-size: 13px;
        font-weight: 700;
        color: #0f172a;
        height: 40px;
        display: flex;
        align-items: center;
        justify-content: center;
    }

    .driver-due-box-zero {
        background: rgba(255, 255, 255, 0.55);
        border: 1.5px solid rgba(255, 255, 255, 0.9);
        border-radius: 14px;
        padding: 6px 6px;
        text-align: center;
        line-height: 1.2;
    }
    .driver-due-box-active {
        background: rgba(254, 226, 226, 0.72);
        border: 1.5px solid rgba(248, 113, 113, 0.6);
        border-radius: 14px;
        padding: 6px 6px;
        text-align: center;
        line-height: 1.2;
    }

    .glass-stat-card {
        background: rgba(255, 255, 255, 0.48);
        backdrop-filter: blur(24px) saturate(190%);
        -webkit-backdrop-filter: blur(24px) saturate(190%);
        border: 1.5px solid rgba(255, 255, 255, 0.85);
        border-radius: 20px;
        padding: 20px 22px;
        box-shadow: 0 8px 24px rgba(15, 23, 42, 0.05), inset 0 1px 1px rgba(255, 255, 255, 0.95);
        height: 100%;
    }
    .stat-label {
        font-size: 15px;
        font-weight: 600;
        color: #475569;
        margin-bottom: 6px;
    }
    .stat-value {
        font-size: 30px;
        font-weight: 700;
        color: #0f172a;
        line-height: 1.15;
    }
    .stat-sub {
        font-size: 14px;
        color: #64748b;
        margin-top: 10px;
        padding-top: 10px;
        border-top: 1px solid rgba(148, 163, 184, 0.25);
    }

    /* ড্রপডাউন মেনু ডিজাইন */
    div[data-testid="stSelectbox"] {
        max-width: 320px !important;
        width: 100% !important;
        min-width: 230px !important;
    }
    div[data-testid="stSelectbox"] label p {
        font-size: 13.5px !important;
        font-weight: 700 !important;
        color: #334155 !important;
        letter-spacing: 0.2px !important;
        margin-bottom: 5px !important;
    }
    div[data-baseweb="select"] > div {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.72) 0%, rgba(240, 247, 255, 0.55) 100%) !important;
        backdrop-filter: blur(28px) saturate(210%) !important;
        -webkit-backdrop-filter: blur(28px) saturate(210%) !important;
        border: 1.5px solid rgba(255, 255, 255, 0.95) !important;
        border-radius: 16px !important;
        padding: 4px 10px !important;
        min-height: 44px !important;
        box-shadow: 0 8px 20px rgba(0, 102, 255, 0.06), inset 0 1px 1px rgba(255, 255, 255, 1) !important;
        font-size: 15px !important;
        font-weight: 600 !important;
        color: #0f172a !important;
    }
    div[data-baseweb="select"] > div > div {
        background: transparent !important;
    }
    div[data-baseweb="popover"], div[data-baseweb="popover"] > div, ul[data-baseweb="menu"], div[role="listbox"] {
        background: rgba(255, 255, 255, 0.92) !important;
        backdrop-filter: blur(36px) saturate(230%) !important;
        -webkit-backdrop-filter: blur(36px) saturate(230%) !important;
        border: 1.5px solid rgba(255, 255, 255, 0.98) !important;
        border-radius: 18px !important;
        box-shadow: 0 18px 42px rgba(15, 23, 42, 0.16), 0 4px 12px rgba(0, 102, 255, 0.08) !important;
        padding: 8px !important;
    }
    ul[data-baseweb="menu"] li, div[role="option"] {
        background: transparent !important;
        border-radius: 12px !important;
        font-size: 14.5px !important;
        font-weight: 600 !important;
        color: #1e293b !important;
        padding: 9px 14px !important;
        margin: 3px 0 !important;
        transition: all 0.15s ease !important;
    }
    ul[data-baseweb="menu"] li:hover, div[role="option"]:hover {
        background: linear-gradient(90deg, rgba(0, 102, 255, 0.16) 0%, rgba(235, 245, 255, 0.95) 100%) !important;
        color: #0066ff !important;
        font-weight: 700 !important;
    }

    div[data-testid="stInput"] input, div[data-baseweb="input"] > div {
        background: rgba(255, 255, 255, 0.65) !important;
        backdrop-filter: blur(18px) !important;
        border: 1.5px solid rgba(255, 255, 255, 0.9) !important;
        border-radius: 14px !important;
        font-size: 15px !important;
        font-weight: 600 !important;
    }

    /* প্রাইমারি অ্যাকশন বাটন */
    section[data-testid="stMain"] button[kind="primary"] {
        background: linear-gradient(180deg, rgba(10, 132, 255, 0.92) 0%, rgba(0, 102, 255, 0.96) 100%) !important;
        backdrop-filter: blur(12px) !important;
        border: 1px solid rgba(255, 255, 255, 0.45) !important;
        border-radius: 14px !important;
        color: #ffffff !important;
        font-size: 14.5px !important;
        font-weight: 600 !important;
        height: 44px !important;
        padding: 0 12px !important;
        box-shadow: 0 4px 12px rgba(0, 102, 255, 0.22), inset 0 1px 0 rgba(255,255,255,0.4) !important;
    }
    section[data-testid="stMain"] button[kind="primary"] p,
    section[data-testid="stMain"] button[kind="secondary"] p {
        font-size: 14.5px !important;
        line-height: 1.15 !important;
        white-space: nowrap !important;
    }

    section[data-testid="stMain"] button[kind="secondary"] {
        background: rgba(255, 255, 255, 0.65) !important;
        backdrop-filter: blur(16px) !important;
        border: 1.5px solid rgba(255, 255, 255, 0.9) !important;
        border-radius: 14px !important;
        color: #1e293b !important;
        font-size: 14.5px !important;
        font-weight: 600 !important;
        height: 44px !important;
        padding: 0 12px !important;
        box-shadow: 0 2px 6px rgba(15, 23, 42, 0.04) !important;
    }
    section[data-testid="stMain"] button[kind="secondary"]:hover {
        background: rgba(255, 255, 255, 0.92) !important;
        color: #0066ff !important;
        border-color: rgba(0, 102, 255, 0.4) !important;
    }

    div[data-testid="stTable"] {
        background: rgba(255, 255, 255, 0.48) !important;
        backdrop-filter: blur(20px) !important;
        border-radius: 16px !important;
        border: 1.5px solid rgba(255, 255, 255, 0.85) !important;
        overflow: hidden !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

if "active_menu" not in st.session_state:
    st.session_state.active_menu = "📊 ড্যাশবোর্ড"

if "drivers_master" not in st.session_state:
    st.session_state.drivers_master = [
        {"নাম": "মোঃ শহিদুল", "ঠিকানা": "মির্জাপুর পুরাতন বাসস্ট্যান্ড", "ফোন": "01700-000001", "ধরন": "নিজস্ব গাড়ি", "গাড়ির_মডেল": "ইজি বাইক (৫ ব্যাটারি)", "নির্ধারিত_জমা": 470, "নির্ধারিত_চার্জ": 0, "নির্ধারিত_ঘর_ভাড়া": 0, "প্রতি_ঘণ্টা_চার্জ": 40},
        {"নাম": "নিজাম উদ্দিন", "ঠিকানা": "বাওয়ার কুমারজানী, মির্জাপুর", "ফোন": "01700-000002", "ধরন": "নিজস্ব গাড়ি", "গাড়ির_মডেল": "ইজি বাইক (৫ ব্যাটারি)", "নির্ধারিত_জমা": 450, "নির্ধারিত_চার্জ": 0, "নির্ধারিত_ঘর_ভাড়া": 0, "প্রতি_ঘণ্টা_চার্জ": 40},
        {"নাম": "কাদের মিয়া", "ঠিকানা": "পোষ্টকামুরী, মির্জাপুর", "ফোন": "01700-000003", "ধরন": "চার্জের গাড়ি", "গাড়ির_মডেল": "মিশুক গাড়ি (৪ ব্যাটারি)", "নির্ধারিত_জমা": 0, "নির্ধারিত_চার্জ": 170, "নির্ধারিত_ঘর_ভাড়া": 50, "প্রতি_ঘণ্টা_চার্জ": 30},
    ]

if "own_cars" not in st.session_state:
    st.session_state.own_cars = []
if "charging_data" not in st.session_state:
    st.session_state.charging_data = []
if "due_recovery" not in st.session_state:
    st.session_state.due_recovery = []
if "extra_income" not in st.session_state:
    st.session_state.extra_income = []
if "daily_expenses" not in st.session_state:
    st.session_state.daily_expenses = []
if "repair_records" not in st.session_state:
    st.session_state.repair_records = []
if "charge_ui_state" not in st.session_state:
    st.session_state.charge_ui_state = {}
if "settings_mode" not in st.session_state:
    st.session_state.settings_mode = "add_car"

# কর্মচারীদের মাস্টার তালিকা ও বেতন সুরক্ষা পাসওয়ার্ড (স্থায়ী পাসওয়ার্ড: 155992)
if "staff_master" not in st.session_state:
    st.session_state.staff_master = [
        {
            "নাম": "গ্যারেজ কর্মচারী",
            "ঠিকানা": "মির্জাপুর, টাঙ্গাইল",
            "ফোন": "01700-000000",
            "মাসিক_বেতন": 20000,
            "বিবরণ": "গ্যারেজ ও চার্জিং স্টেশন দেখাশোনা"
        }
    ]
if "staff_salary_payments" not in st.session_state:
    st.session_state.staff_salary_payments = []
if "edit_staff_target" not in st.session_state:
    st.session_state.edit_staff_target = None

# কর্মচারীর বেতন/তথ্য ডিলিট করার পাসওয়ার্ড প্রোটেকশন স্টেট
if "admin_delete_pin" not in st.session_state:
    st.session_state.admin_delete_pin = "155992"
if "pending_salary_del_idx" not in st.session_state:
    st.session_state.pending_salary_del_idx = None
if "pending_staff_del_idx" not in st.session_state:
    st.session_state.pending_staff_del_idx = None

# ডিলিট, এডিট, এবং এন্ট্রি রিসেট স্টেট
if "delete_target" not in st.session_state:
    st.session_state.delete_target = None
if "delete_step" not in st.session_state:
    st.session_state.delete_step = 0
if "edit_target" not in st.session_state:
    st.session_state.edit_target = None
if "reset_entry_target" not in st.session_state:
    st.session_state.reset_entry_target = None
if "reset_entry_type" not in st.session_state:
    st.session_state.reset_entry_type = None

if "new_car_model_sel" not in st.session_state:
    st.session_state.new_car_model_sel = "মিশুক গাড়ি (৪ ব্যাটারি)"

# --- ফাংশনসমূহ ---
def save_or_update_own_car(driver_name, status, joma_amt, baki_amt):
    for item in st.session_state.own_cars:
        if item["চালক"] == driver_name:
            item["অবস্থা"] = status
            item["জমা"] = joma_amt
            item["বাকি"] = baki_amt
            return
    st.session_state.own_cars.append({
        "চালক": driver_name,
        "অবস্থা": status,
        "জমা": joma_amt,
        "বাকি": baki_amt
    })

def get_driver_ui_pref(driver_name):
    if driver_name not in st.session_state.charge_ui_state:
        st.session_state.charge_ui_state[driver_name] = {
            "mode": "চার্জ বিল",
            "hours": 0
        }
    return st.session_state.charge_ui_state[driver_name]

def commit_charging_transaction(driver_name, mode, action_type, base_amt, extra_hrs, extra_amt):
    total_amt = base_amt + extra_amt
    paid_amt = total_amt if action_type == "আদায়" else 0
    due_amt = total_amt if action_type == "বাকি" else 0

    existing = next((item for item in st.session_state.charging_data if item["চালক"] == driver_name), None)
    if existing is None:
        existing = {
            "চালক": driver_name,
            "চার্জ_অবস্থা": "-",
            "চার্জ_জমা": 0,
            "চার্জ_বাকি": 0,
            "অতিরিক্ত_ঘণ্টা": 0,
            "অতিরিক্ত_বিল": 0,
            "ঘর_ভাড়া_অবস্থা": "-",
            "ঘর_ভাড়া_জমা": 0,
            "ঘর_ভাড়া_বাকি": 0
        }
        st.session_state.charging_data.append(existing)

    existing["অতিরিক্ত_ঘণ্টা"] = extra_hrs
    existing["অতিরিক্ত_বিল"] = extra_amt

    if mode == "চার্জ বিল":
        existing["চার্জ_অবস্থা"] = f"চার্জ বিল {action_type}"
        existing["চার্জ_জমা"] = paid_amt
        existing["চার্জ_বাকি"] = due_amt
        existing["ঘর_ভাড়া_অবস্থা"] = "-"
        existing["ঘর_ভাড়া_জমা"] = 0
        existing["ঘর_ভাড়া_বাকি"] = 0
    else:
        existing["ঘর_ভাড়া_অবস্থা"] = f"ঘর ভাড়া {action_type}"
        existing["ঘর_ভাড়া_জমা"] = paid_amt
        existing["ঘর_ভাড়া_বাকি"] = due_amt
        existing["চার্জ_অবস্থা"] = "-"
        existing["চার্জ_জমা"] = 0
        existing["চার্জ_বাকি"] = 0

# --- হিসাব গণনা ---
own_car_paid = sum(item["জমা"] for item in st.session_state.own_cars)
own_car_due = sum(item["বাকি"] for item in st.session_state.own_cars)
own_received_count = sum(1 for item in st.session_state.own_cars if item["অবস্থা"] == "জমা আদায়")
own_due_count = sum(1 for item in st.session_state.own_cars if item["অবস্থা"] == "জমা বাকি")
own_absent_count = sum(1 for item in st.session_state.own_cars if item["অবস্থা"] == "অনুপস্থিত")

charge_bill_paid = sum(item["চার্জ_জমা"] for item in st.session_state.charging_data)
charge_bill_due = sum(item["চার্জ_বাকি"] for item in st.session_state.charging_data)
extra_hourly_total = sum(item.get("অতিরিক্ত_বিল", 0) for item in st.session_state.charging_data)
garage_rent_paid = sum(item["ঘর_ভাড়া_জমা"] for item in st.session_state.charging_data)
garage_rent_due = sum(item["ঘর_ভাড়া_বাকি"] for item in st.session_state.charging_data)

total_charge_drivers = len([d for d in st.session_state.drivers_master if d["ধরন"] == "চার্জের গাড়ি"])
charged_count = sum(1 for item in st.session_state.charging_data if item["চার্জ_অবস্থা"] != "-" or item["ঘর_ভাড়া_অবস্থা"] != "-")
not_charged_count = max(0, total_charge_drivers - charged_count)

rec_own = sum(item["আদায়_টাকা"] for item in st.session_state.due_recovery if item["খাত"] == "নিজস্ব গাড়ির জমার বাকি")
rec_charge = sum(item["আদায়_টাকা"] for item in st.session_state.due_recovery if item["খাত"] == "চার্জের বিলের বাকি")
rec_rent = sum(item["আদায়_টাকা"] for item in st.session_state.due_recovery if item["খাত"] == "চার্জের গাড়ির ঘর ভাড়ার বাকি")
total_recovered = rec_own + rec_charge + rec_rent

repair_paid_total = sum(r["টাকা"] for r in st.session_state.repair_records if r["ধরণ"] == "আদায়")
repair_due_total = sum(r["টাকা"] for r in st.session_state.repair_records if r["ধরণ"] == "বাকি")

total_extra_income = sum(item["টাকা"] for item in st.session_state.extra_income)

# দৈনিক খরচের হিসাব
total_daily_expense = sum(item["টাকা"] for item in st.session_state.daily_expenses)

# কর্মচারীর বেতনের সামগ্রিক হিসাব
total_staff_monthly_budget = sum(s["মাসিক_বেতন"] for s in st.session_state.staff_master)
total_staff_paid = sum(p["টাকা"] for p in st.session_state.staff_salary_payments)
remaining_staff_salary = max(0, total_staff_monthly_budget - total_staff_paid)

net_own_due = max(0, own_car_due - rec_own)
net_charge_due = max(0, charge_bill_due - rec_charge)
net_rent_due = max(0, garage_rent_due - rec_rent)

grand_total_due = net_own_due + net_charge_due + net_rent_due
gross_total_cash = own_car_paid + charge_bill_paid + garage_rent_paid + total_recovered + total_extra_income + repair_paid_total
net_cash_in_hand = gross_total_cash - (total_staff_paid + total_daily_expense)

# --- বাম পাশের প্রিমিয়াম লিকুইড গ্লাস মেনু ---
menu_items = [
    ("📊 ড্যাশবোর্ড", "menu_nav_dash"),
    ("💳 জমা আদায়", "menu_nav_joma"),
    ("🧾 বাকি আদায়", "menu_nav_baki"),
    ("💰 অতিরিক্ত আয়", "menu_nav_extra"),
    ("💸 দৈনিক খরচ", "menu_nav_expense"),
    ("👷 কর্মচারীর বেতন", "menu_nav_staff_sal"),
    ("⚙️ সেটিংস", "menu_nav_settings")
]

with st.sidebar:
    st.markdown(
        """
        <div class="sidebar-brand-box">
            <div class="sidebar-brand-title">☰ মেনু</div>
            <div class="sidebar-brand-sub">নেভিগেশন প্যানেল</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    for label_txt, btn_key in menu_items:
        is_active = (st.session_state.active_menu == label_txt)
        if st.button(
            label_txt,
            key=btn_key,
            type="primary" if is_active else "secondary",
            use_container_width=True
        ):
            st.session_state.active_menu = label_txt
            st.rerun()

    st.markdown(
        f"<div style='margin-top:26px; padding:12px 14px; border-radius:16px; "
        f"background:rgba(255,255,255,0.62); border:1.5px solid rgba(255,255,255,0.92); "
        f"box-shadow:0 4px 14px rgba(15,23,42,0.04); font-size:13.5px; color:#334155; text-align:center;'>"
        f"📅 আজকের তারিখ<br><b style='font-size:15px; color:#0066ff;'>{date.today().strftime('%d-%m-%Y')}</b></div>",
        unsafe_allow_html=True
    )

selected_menu = st.session_state.active_menu

# --- প্রফেশনাল টপ অ্যাপ-বার ---
due_badge_html = (
    '<div class="due-pill-zero">● বকেয়া শূন্য (০ ৳)</div>'
    if grand_total_due == 0
    else f'<div class="due-pill-active">● মোট বকেয়া: {grand_total_due} ৳</div>'
)

st.markdown(
    f"""
    <div class="pro-header">
        <div>
            <div class="pro-title">⚡ গ্যারেজ ও চার্জিং স্টেশন ম্যানেজার</div>
            <div class="pro-subtitle">দৈনিক হিসাব, জমা ও বকেয়া নিয়ন্ত্রণ প্যানেল • তারিখ: {date.today().strftime('%d-%m-%Y')}</div>
        </div>
        {due_badge_html}
    </div>
    """,
    unsafe_allow_html=True
)

own_drivers = [d for d in st.session_state.drivers_master if d["ধরন"] == "নিজস্ব গাড়ি"]
charge_drivers = [d for d in st.session_state.drivers_master if d["ধরন"] == "চার্জের গাড়ি"]

# ==================== ১. ড্যাশবোর্ড ====================
if selected_menu == "📊 ড্যাশবোর্ড":
    st.markdown(
        f"""
        <div class="glass-stat-card" style="margin-bottom: 18px; background: linear-gradient(135deg, rgba(255,255,255,0.65), rgba(235,245,255,0.55));">
            <div class="stat-label">সর্বমোট নিট নগদ ক্যাশ (মোট আয়: {gross_total_cash:,}৳ − দৈনিক খরচ: {total_daily_expense:,}৳ − বেতন: {total_staff_paid:,}৳)</div>
            <div class="stat-value" style="color: #0066ff; font-size: 36px;">{net_cash_in_hand:,} ৳</div>
            <div class="stat-sub">সব খাতের জমা ও আয় থেকে দৈনিক খরচ ও কর্মচারীর বেতন বাদে হাতে থাকা নিট ক্যাশ</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown(
            f"""
            <div class="glass-stat-card">
                <div class="stat-label">🚙 নিজস্ব গাড়ির জমা</div>
                <div class="stat-value">{own_car_paid + rec_own} ৳</div>
                <div class="stat-sub">
                    বাকি: <b style="color:#dc2626;">{net_own_due} ৳</b><br>
                    আদায়: {own_received_count} • বাকি: {own_due_count} • অনুপস্থিত: {own_absent_count}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
    with c2:
        st.markdown(
            f"""
            <div class="glass-stat-card">
                <div class="stat-label">⚡ চার্জের বিল (তালিকাভুক্ত)</div>
                <div class="stat-value">{charge_bill_paid + rec_charge} ৳</div>
                <div class="stat-sub">
                    বাকি: <b style="color:#dc2626;">{net_charge_due} ৳</b><br>
                    এন্ট্রি হয়েছে: {charged_count} টি • বাকি আছে: {not_charged_count} টি
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
    with c3:
        st.markdown(
            f"""
            <div class="glass-stat-card">
                <div class="stat-label">💸 আজকের দৈনিক খরচ</div>
                <div class="stat-value" style="color:#dc2626;">{total_daily_expense:,} ৳</div>
                <div class="stat-sub">
                    মোট খরচের এন্ট্রি: <b>{len(st.session_state.daily_expenses)} টি</b><br>
                    ঘর ভাড়া জমা: {garage_rent_paid + rec_rent} ৳
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
    with c4:
        st.markdown(
            f"""
            <div class="glass-stat-card">
                <div class="stat-label">👷 কর্মচারীর অবশিষ্ট বেতন</div>
                <div class="stat-value" style="color:#d97706;">{remaining_staff_salary:,} ৳</div>
                <div class="stat-sub">
                    মাসিক: {total_staff_monthly_budget:,}৳ • পরিশোধিত: {total_staff_paid:,}৳
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

# ==================== ২. জমা আদায় ====================
elif selected_menu == "💳 জমা আদায়":
    selected_category = st.selectbox(
        "গাড়ির ধরন নির্বাচন করুন",
        ["নিজস্ব গাড়ি", "চার্জের গাড়ি"],
        key="tab2_car_type_select"
    )
    st.markdown("<div style='height: 6px;'></div>", unsafe_allow_html=True)

    if st.session_state.reset_entry_target is not None:
        r_name = st.session_state.reset_entry_target
        r_type = st.session_state.reset_entry_type
        with st.container(border=True):
            st.warning(f"⚠️ **পারমিশন প্রয়োজন:** আপনি কি নিশ্চিতভাবে **{r_name}**-এর আজকের ভুল এন্ট্রিটি মুছে পুনরায় **ব্ল্যাঙ্ক (ফাঁকা)** করতে চান?")
            rc1, rc2, _ = st.columns([1.5, 1.1, 2.8])
            if rc1.button("✅ হ্যাঁ, ব্ল্যাঙ্ক করুন", key="confirm_reset_entry", type="primary", use_container_width=True):
                if r_type == "own":
                    st.session_state.own_cars = [x for x in st.session_state.own_cars if x["চালক"] != r_name]
                elif r_type == "charging":
                    st.session_state.charging_data = [x for x in st.session_state.charging_data if x["চালক"] != r_name]
                    if r_name in st.session_state.charge_ui_state:
                        st.session_state.charge_ui_state[r_name]["hours"] = 0
                st.session_state.reset_entry_target = None
                st.session_state.reset_entry_type = None
                st.rerun()
            if rc2.button("বাতিল করুন", key="cancel_reset_entry", use_container_width=True):
                st.session_state.reset_entry_target = None
                st.session_state.reset_entry_type = None
                st.rerun()

    # ১. নিজস্ব গাড়ি
    if selected_category == "নিজস্ব গাড়ি":
        if not own_drivers:
            st.info("কোনো নিজস্ব গাড়ির চালক যোগ করা নেই। বাম পাশের মেনু থেকে '⚙️ সেটিংস'-এ গিয়ে যুক্ত করুন।")
        else:
            for idx, d_info in enumerate(own_drivers):
                fixed_joma = d_info["নির্ধারিত_জমা"]
                car_model = d_info.get("গাড়ির_মডেল", "ইজি বাইক (৫ ব্যাটারি)")
                existing_own = next((x for x in st.session_state.own_cars if x["চালক"] == d_info["নাম"]), None)
                
                driver_rec = sum(r["আদায়_টাকা"] for r in st.session_state.due_recovery if r["চালক"] == d_info["নাম"] and r["খাত"] == "নিজস্ব গাড়ির জমার বাকি")
                driver_total_due = max(0, (existing_own["বাকি"] if existing_own else 0) - driver_rec)

                badge_html = ""
                if existing_own:
                    st_txt = existing_own["অবস্থা"]
                    bg_col = "#dcfce7" if st_txt == "জমা আদায়" else ("#fee2e2" if st_txt == "জমা বাকি" else "#f1f5f9")
                    tx_col = "#166534" if st_txt == "জমা আদায়" else ("#991b1b" if st_txt == "জমা বাকি" else "#475569")
                    badge_html = f"<span style='background:{bg_col}; color:{tx_col}; padding:2px 8px; border-radius:99px; font-size:12px; font-weight:600; margin-left:6px;'>{st_txt}</span>"

                phone_txt = f" • 📞 {d_info.get('ফোন', '')}" if d_info.get("ফোন") else ""

                with st.container(border=True):
                    col_name, col_b1, col_b2, col_b3, col_due_box, col_reset = st.columns([2.2, 1.15, 1.15, 0.95, 1.05, 0.45], gap="small")
                    with col_name:
                        st.markdown(
                            f"<div style='font-size:17px; font-weight:700; color:#0f172a;'>{idx + 1}. {d_info['নাম']}{badge_html}</div>"
                            f"<div style='font-size:12.5px; color:#64748b;'>🚘 {car_model} • জমা: <b>{fixed_joma}৳</b> • 📍 {d_info['ঠিকানা']}{phone_txt}</div>",
                            unsafe_allow_html=True
                        )

                    if col_b1.button(f"জমা আদায় ({fixed_joma}৳)", key=f"own_paid_{idx}", use_container_width=True, type="primary"):
                        save_or_update_own_car(d_info["নাম"], "জমা আদায়", fixed_joma, 0)
                        st.rerun()

                    if col_b2.button(f"জমা বাকি ({fixed_joma}৳)", key=f"own_due_{idx}", use_container_width=True):
                        save_or_update_own_car(d_info["নাম"], "জমা বাকি", 0, fixed_joma)
                        st.rerun()

                    if col_b3.button("অনুপস্থিত", key=f"own_abs_{idx}", use_container_width=True):
                        save_or_update_own_car(d_info["নাম"], "অনুপস্থিত", 0, 0)
                        st.rerun()

                    with col_due_box:
                        box_cls = "driver-due-box-active" if driver_total_due > 0 else "driver-due-box-zero"
                        val_col = "#dc2626" if driver_total_due > 0 else "#475569"
                        st.markdown(
                            f"<div class='{box_cls}'>"
                            f"<div style='font-size:11px; color:#64748b; font-weight:600;'>মোট বাকি</div>"
                            f"<div style='font-size:16px; color:{val_col}; font-weight:700;'>{driver_total_due} ৳</div>"
                            f"</div>",
                            unsafe_allow_html=True
                        )

                    with col_reset:
                        if existing_own:
                            if st.button("↺", key=f"reset_own_{idx}", help="ভুল এন্ট্রি মুছে পুনরায় ব্ল্যাঙ্ক করুন", use_container_width=True):
                                st.session_state.reset_entry_target = d_info["নাম"]
                                st.session_state.reset_entry_type = "own"
                                st.rerun()

        if st.session_state.own_cars:
            st.markdown("<div style='height: 12px;'></div>", unsafe_allow_html=True)
            st.markdown("#### আজকের নিজস্ব গাড়ির জমার তালিকা")
            st.table(st.session_state.own_cars)

    # ২. চার্জের গাড়ি
    else:
        if not charge_drivers:
            st.info("কোনো চার্জের গাড়ির চালক যোগ করা নেই। বাম পাশের মেনু থেকে '⚙️ সেটিংস'-এ গিয়ে যুক্ত করুন।")
        else:
            for idx, d_info in enumerate(charge_drivers):
                fixed_charge = d_info["নির্ধারিত_চার্জ"]
                fixed_rent = d_info["নির্ধারিত_ঘর_ভাড়া"]
                hourly_rate = d_info.get("প্রতি_ঘণ্টা_চার্জ", 30)
                car_model = d_info.get("গাড়ির_মডেল", "মিশুক গাড়ি (৪ ব্যাটারি)")

                ui_pref = get_driver_ui_pref(d_info["নাম"])
                selected_mode = ui_pref["mode"]
                selected_hrs = ui_pref["hours"]

                base_amount = fixed_charge if selected_mode == "চার্জ বিল" else fixed_rent
                extra_amount = selected_hrs * hourly_rate
                final_payable = base_amount + extra_amount

                existing_chg = next((x for x in st.session_state.charging_data if x["চালক"] == d_info["নাম"]), None)
                raw_chg_due = existing_chg["চার্জ_বাকি"] if existing_chg else 0
                raw_rent_due = existing_chg["ঘর_ভাড়া_বাকি"] if existing_chg else 0

                driver_rec = sum(
                    r["আদায়_টাকা"] for r in st.session_state.due_recovery
                    if r["চালক"] == d_info["নাম"] and r["খাত"] in ["চার্জের বিলের বাকি", "চার্জের গাড়ির ঘর ভাড়ার বাকি"]
                )
                driver_total_due = max(0, (raw_chg_due + raw_rent_due) - driver_rec)

                badge_html = ""
                if existing_chg:
                    active_status = existing_chg["চার্জ_অবস্থা"] if existing_chg["চার্জ_অবস্থা"] != "-" else existing_chg["ঘর_ভাড়া_অবস্থা"]
                    if active_status != "-":
                        saved_amt = max(existing_chg["চার্জ_জমা"], existing_chg["চার্জ_বাকি"], existing_chg["ঘর_ভাড়া_জমা"], existing_chg["ঘর_ভাড়া_বাকি"])
                        hrs_info = f" (+{existing_chg['অতিরিক্ত_ঘণ্টা']}ঘণ্টা)" if existing_chg.get("অতিরিক্ত_ঘণ্টা", 0) > 0 else ""
                        is_due_st = "বাকি" in active_status
                        bg_c = "#fee2e2" if is_due_st else "#dcfce7"
                        tx_c = "#991b1b" if is_due_st else "#166534"
                        badge_html = f"<span style='background:{bg_c}; color:{tx_c}; padding:3px 10px; border-radius:99px; font-size:12px; font-weight:700; margin-left:8px;'>✓ {active_status}: {saved_amt}৳{hrs_info}</span>"

                phone_txt = f" • 📞 {d_info.get('ফোন', '')}" if d_info.get("ফোন") else ""

                with st.container(border=True):
                    c_info, c_mode, c_hrs, c_action, c_due, c_rst = st.columns(
                        [2.0, 2.05, 1.45, 2.15, 0.85, 0.35],
                        gap="small"
                    )

                    with c_info:
                        st.markdown(
                            f"<div style='font-size:17px; font-weight:700; color:#0f172a; margin-top:2px;'>{idx + 1}. {d_info['নাম']}{badge_html}</div>"
                            f"<div style='font-size:12.5px; color:#64748b; margin-top:3px;'>🚘 {car_model} • ⚡ {fixed_charge}৳ | 🏠 {fixed_rent}৳{phone_txt}</div>",
                            unsafe_allow_html=True
                        )

                    with c_mode:
                        st.markdown("<div class='step-mini-label'>১. খাত বেছে নিন</div>", unsafe_allow_html=True)
                        m1, m2 = st.columns(2, gap="small")
                        if m1.button(
                            f"⚡ চার্জ {fixed_charge}৳",
                            key=f"mode_chg_{idx}",
                            type="primary" if selected_mode == "চার্জ বিল" else "secondary",
                            use_container_width=True
                        ):
                            st.session_state.charge_ui_state[d_info["নাম"]]["mode"] = "চার্জ বিল"
                            st.rerun()

                        if m2.button(
                            f"🏠 ভাড়া {fixed_rent}৳",
                            key=f"mode_rent_{idx}",
                            type="primary" if selected_mode == "ঘর ভাড়া" else "secondary",
                            use_container_width=True
                        ):
                            st.session_state.charge_ui_state[d_info["নাম"]]["mode"] = "ঘর ভাড়া"
                            st.rerun()

                    with c_hrs:
                        st.markdown(f"<div class='step-mini-label'>২. অতিরিক্ত ({hourly_rate}৳/ঘঃ)</div>", unsafe_allow_html=True)
                        h_minus, h_val, h_plus = st.columns([0.85, 1.55, 0.85], gap="small")
                        if h_minus.button("➖", key=f"hr_dec_{idx}", use_container_width=True):
                            if selected_hrs > 0:
                                st.session_state.charge_ui_state[d_info["নাম"]]["hours"] = selected_hrs - 1
                                st.rerun()
                        with h_val:
                            hr_text = f"{selected_hrs}ঘঃ (+{extra_amount}৳)" if selected_hrs > 0 else "০ ঘণ্টা"
                            st.markdown(f"<div class='extra-hour-pill'>{hr_text}</div>", unsafe_allow_html=True)
                        if h_plus.button("➕", key=f"hr_inc_{idx}", use_container_width=True):
                            if selected_hrs < 12:
                                st.session_state.charge_ui_state[d_info["নাম"]]["hours"] = selected_hrs + 1
                                st.rerun()

                    with c_action:
                        st.markdown(f"<div class='step-mini-label'>৩. {selected_mode} সেভ করুন</div>", unsafe_allow_html=True)
                        a1, a2 = st.columns(2, gap="small")
                        if a1.button(
                            f"✅ আদায় ({final_payable}৳)",
                            key=f"act_paid_{idx}",
                            type="primary",
                            use_container_width=True
                        ):
                            commit_charging_transaction(d_info["নাম"], selected_mode, "আদায়", base_amount, selected_hrs, extra_amount)
                            st.rerun()

                        if a2.button(
                            f"⏳ বাকি ({final_payable}৳)",
                            key=f"act_due_{idx}",
                            type="secondary",
                            use_container_width=True
                        ):
                            commit_charging_transaction(d_info["নাম"], selected_mode, "বাকি", base_amount, selected_hrs, extra_amount)
                            st.rerun()

                    with c_due:
                        st.markdown("<div class='step-mini-label'>&nbsp;</div>", unsafe_allow_html=True)
                        box_cls = "driver-due-box-active" if driver_total_due > 0 else "driver-due-box-zero"
                        val_col = "#dc2626" if driver_total_due > 0 else "#475569"
                        st.markdown(
                            f"<div class='{box_cls}'>"
                            f"<div style='font-size:10px; color:#64748b; font-weight:600;'>মোট বাকি</div>"
                            f"<div style='font-size:14.5px; color:{val_col}; font-weight:700;'>{driver_total_due} ৳</div>"
                            f"</div>",
                            unsafe_allow_html=True
                        )

                    with c_rst:
                        st.markdown("<div class='step-mini-label'>&nbsp;</div>", unsafe_allow_html=True)
                        if existing_chg:
                            if st.button("↺", key=f"reset_chg_{idx}", help="ভুল এন্ট্রি মুছে পুনরায় ব্ল্যাঙ্ক করুন", use_container_width=True):
                                st.session_state.reset_entry_target = d_info["নাম"]
                                st.session_state.reset_entry_type = "charging"
                                st.rerun()

        if st.session_state.charging_data:
            st.markdown("<div style='height: 12px;'></div>", unsafe_allow_html=True)
            st.markdown("#### আজকের চার্জের গাড়ির বিল ও ঘর ভাড়ার তালিকা")
            st.table(st.session_state.charging_data)

# ==================== ৩. বাকি আদায় ====================
elif selected_menu == "🧾 বাকি আদায়":
    d1, d2, d3 = st.columns(3)
    with d1:
        st.markdown(f"<div class='glass-stat-card'><div class='stat-label'>নিজস্ব গাড়ির জমার বাকি</div><div class='stat-value' style='color:#dc2626;'>{net_own_due} ৳</div></div>", unsafe_allow_html=True)
    with d2:
        st.markdown(f"<div class='glass-stat-card'><div class='stat-label'>চার্জের বিলের বাকি</div><div class='stat-value' style='color:#dc2626;'>{net_charge_due} ৳</div></div>", unsafe_allow_html=True)
    with d3:
        st.markdown(f"<div class='glass-stat-card'><div class='stat-label'>ঘর ভাড়ার বাকি (সংযুক্ত চার্জসহ)</div><div class='stat-value' style='color:#dc2626;'>{net_rent_due} ৳</div></div>", unsafe_allow_html=True)

    st.markdown("<div style='height: 16px;'></div>", unsafe_allow_html=True)

    with st.form("recovery_form", clear_on_submit=True):
        f1, f2, f3 = st.columns(3)
        rec_category = f1.selectbox("কোন খাতের বাকি আদায়?", [
            "নিজস্ব গাড়ির জমার বাকি",
            "চার্জের বিলের বাকি",
            "চার্জের গাড়ির ঘর ভাড়ার বাকি"
        ], index=None, placeholder="খাত নির্বাচন করুন...", key="tab3_rec_category")
        ordered_all_names = [d["নাম"] for d in (own_drivers + charge_drivers)]
        rec_name = f2.selectbox("চালকের নাম নির্বাচন করুন", ordered_all_names, index=None, placeholder="চালক নির্বাচন করুন...", key="tab3_rec_name")
        rec_amount = f3.number_input("আদায়কৃত টাকা (৳)", min_value=0, step=10, key="tab3_rec_amount")

        if st.form_submit_button("বাকি আদায় সেভ করুন", type="primary"):
            if rec_category and rec_name and rec_amount > 0:
                st.session_state.due_recovery.append({
                    "খাত": rec_category,
                    "চালক": rec_name,
                    "আদায়_টাকা": rec_amount
                })
                st.rerun()
            else:
                st.warning("দয়া করে খাত, চালকের নাম এবং টাকার পরিমাণ সঠিকভাবে নির্বাচন করুন।")

    all_dues_list = []
    for item in st.session_state.own_cars:
        if item["বাকি"] > 0:
            all_dues_list.append({"খাত": "নিজস্ব গাড়ির জমার বাকি", "চালক": item["চালক"], "বাকি_টাকা": item["বাকি"]})
    for item in st.session_state.charging_data:
        if item["চার্জ_বাকি"] > 0:
            all_dues_list.append({"খাত": "চার্জের বিলের বাকি", "চালক": item["চালক"], "বাকি_টাকা": item["চার্জ_বাকি"]})
        if item["ঘর_ভাড়া_বাকি"] > 0:
            all_dues_list.append({"খাত": "চার্জের গাড়ির ঘর ভাড়ার বাকি", "চালক": item["চালক"], "বাকি_টাকা": item["ঘর_ভাড়া_বাকি"]})

    if all_dues_list:
        st.markdown("#### বর্তমান বকেয়া তালিকা")
        st.table(all_dues_list)

    if st.session_state.due_recovery:
        st.markdown("#### আজকের আদায়কৃত বকেয়া")
        st.table(st.session_state.due_recovery)

# ==================== ৪. 💰 অতিরিক্ত আয় ====================
elif selected_menu == "💰 অতিরিক্ত আয়":
    cat_charge_bill = sum(x["টাকা"] for x in st.session_state.extra_income if x["খাত"] == "বাহিরের গাড়ি চার্জ বিল")
    cat_repair = sum(x["টাকা"] for x in st.session_state.extra_income if x["খাত"] == "চার্জার মেরামত")
    cat_water_acid = sum(x["টাকা"] for x in st.session_state.extra_income if x["খাত"] in ["পানি বিক্রি", "এসি বিক্রি"])
    cat_others = sum(x["টাকা"] for x in st.session_state.extra_income if x["খাত"] == "অন্যান্য অতিরিক্ত ইনকাম")

    e1, e2, e3, e4 = st.columns(4)
    with e1:
        st.markdown(f"<div class='glass-stat-card'><div class='stat-label'>💰 মোট অতিরিক্ত আয়</div><div class='stat-value' style='color:#059669;'>{total_extra_income} ৳</div></div>", unsafe_allow_html=True)
    with e2:
        st.markdown(f"<div class='glass-stat-card'><div class='stat-label'>⚡ বাহিরের গাড়ি চার্জ বিল</div><div class='stat-value'>{cat_charge_bill} ৳</div></div>", unsafe_allow_html=True)
    with e3:
        st.markdown(f"<div class='glass-stat-card'><div class='stat-label'>🔧 চার্জার মেরামত</div><div class='stat-value'>{cat_repair} ৳</div></div>", unsafe_allow_html=True)
    with e4:
        st.markdown(f"<div class='glass-stat-card'><div class='stat-label'>💧 পানি / এসি / অন্যান্য</div><div class='stat-value'>{cat_water_acid + cat_others} ৳</div></div>", unsafe_allow_html=True)

    st.markdown("<div style='height: 16px;'></div>", unsafe_allow_html=True)
    st.markdown("### ➕ নতুন অতিরিক্ত আয় যোগ করুন")

    with st.form("extra_income_form", clear_on_submit=True):
        ex1, ex2, ex3 = st.columns([1.4, 1.8, 1.0])
        income_category = ex1.selectbox(
            "আয়ের খাত নির্বাচন করুন",
            [
                "বাহিরের গাড়ি চার্জ বিল",
                "চার্জার মেরামত",
                "পানি বিক্রি",
                "এসি বিক্রি",
                "অন্যান্য অতিরিক্ত ইনকাম"
            ],
            index=None,
            placeholder="খাত নির্বাচন করুন...",
            key="extra_income_cat"
        )
        income_note = ex2.text_input(
            "বিবরণ / কাস্টমারের নাম (ঐচ্ছিক)",
            placeholder="যেমন: ২ বোতল পানি, বা গাড়ির নম্বর / নাম",
            key="extra_income_note"
        )
        income_amount = ex3.number_input(
            "আদায়কৃত টাকা (৳)",
            min_value=0,
            step=10,
            key="extra_income_amt"
        )

        if st.form_submit_button("💾 অতিরিক্ত আয় সেভ করুন", type="primary"):
            if income_category is None:
                st.warning("দয়া করে আগে একটি আয়ের খাত নির্বাচন করুন।")
            elif income_amount <= 0:
                st.warning("দয়া করে আদায়কৃত টাকার পরিমাণ লিখুন।")
            else:
                st.session_state.extra_income.append({
                    "তারিখ": date.today().strftime("%d-%m-%Y"),
                    "খাত": income_category,
                    "বিবরণ": income_note.strip() if income_note.strip() else "-",
                    "টাকা": income_amount
                })
                st.success(f"✅ {income_category} বাবদ {income_amount} ৳ সফলভাবে সেভ হয়েছে!")
                st.rerun()

    if st.session_state.extra_income:
        st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)
        st.markdown("#### 📋 আজকের অতিরিক্ত আয়ের তালিকা")
        for idx in range(len(st.session_state.extra_income) - 1, -1, -1):
            row = st.session_state.extra_income[idx]
            with st.container(border=True):
                c_txt, c_amt, c_del = st.columns([3.8, 1.2, 0.7], gap="small")
                with c_txt:
                    st.markdown(
                        f"<div style='font-size:16px; font-weight:700; color:#0f172a;'>{idx + 1}. {row['খাত']}</div>"
                        f"<div style='font-size:13px; color:#64748b;'>📝 বিবরণ: {row['বিবরণ']} • 📅 {row['তারিখ']}</div>",
                        unsafe_allow_html=True
                    )
                with c_amt:
                    st.markdown(
                        f"<div style='font-size:18px; font-weight:700; color:#059669; text-align:right; padding-top:6px;'>+{row['টাকা']} ৳</div>",
                        unsafe_allow_html=True
                    )
                with c_del:
                    if st.button("🗑️", key=f"del_extra_inc_{idx}", help="ভুল এন্ট্রি মুছুন", use_container_width=True):
                        st.session_state.extra_income.pop(idx)
                        st.rerun()
    else:
        st.info("আজকে এখনো কোনো অতিরিক্ত আয়ের এন্ট্রি দেওয়া হয়নি।")

# ==================== ৫. 💸 দৈনিক খরচ (নতুন মেনু) ====================
elif selected_menu == "💸 দৈনিক খরচ":
    exp_parts = sum(x["টাকা"] for x in st.session_state.daily_expenses if x["খাত"] == "গাড়ির পার্টস ও মেরামত")
    exp_snacks = sum(x["টাকা"] for x in st.session_state.daily_expenses if x["খাত"] == "চা-নাস্তা ও আপ্যায়ন")
    exp_electric_rent = sum(x["টাকা"] for x in st.session_state.daily_expenses if x["খাত"] in ["বিদ্যুৎ বিল", "গ্যারেজ ভাড়া"])
    exp_others = sum(x["টাকা"] for x in st.session_state.daily_expenses if x["খাত"] == "অন্যান্য খরচ")

    ex_c1, ex_c2, ex_c3, ex_c4 = st.columns(4)
    with ex_c1:
        st.markdown(f"<div class='glass-stat-card'><div class='stat-label'>💸 মোট দৈনিক খরচ</div><div class='stat-value' style='color:#dc2626;'>{total_daily_expense:,} ৳</div></div>", unsafe_allow_html=True)
    with ex_c2:
        st.markdown(f"<div class='glass-stat-card'><div class='stat-label'>🔧 পার্টস ও মেরামত</div><div class='stat-value'>{exp_parts:,} ৳</div></div>", unsafe_allow_html=True)
    with ex_c3:
        st.markdown(f"<div class='glass-stat-card'><div class='stat-label'>☕ চা-নাস্তা ও আপ্যায়ন</div><div class='stat-value'>{exp_snacks:,} ৳</div></div>", unsafe_allow_html=True)
    with ex_c4:
        st.markdown(f"<div class='glass-stat-card'><div class='stat-label'>⚡ বিদ্যুৎ / ভাড়া / অন্যান্য</div><div class='stat-value'>{exp_electric_rent + exp_others:,} ৳</div></div>", unsafe_allow_html=True)

    st.markdown("<div style='height: 16px;'></div>", unsafe_allow_html=True)
    st.markdown("### ➕ নতুন দৈনিক খরচ যোগ করুন")

    with st.form("daily_expense_form", clear_on_submit=True):
        d_ex1, d_ex2, d_ex3, d_ex4 = st.columns([1.1, 1.4, 1.7, 1.0])
        exp_date = d_ex1.date_input("তারিখ", value=date.today(), key="daily_exp_date")
        exp_category = d_ex2.selectbox(
            "খরচের খাত নির্বাচন করুন",
            [
                "গাড়ির পার্টস ও মেরামত",
                "চা-নাস্তা ও আপ্যায়ন",
                "বিদ্যুৎ বিল",
                "গ্যারেজ ভাড়া",
                "অন্যান্য খরচ"
            ],
            index=None,
            placeholder="খাত নির্বাচন করুন...",
            key="daily_exp_cat"
        )
        exp_note = d_ex3.text_input(
            "খরচের বিবরণ (ঐচ্ছিক)",
            placeholder="যেমন: ২টি চাকা মেরামত বা চা-বিস্কুট",
            key="daily_exp_note"
        )
        exp_amount = d_ex4.number_input(
            "খরচের টাকা (৳)",
            min_value=0,
            step=10,
            key="daily_exp_amt"
        )

        if st.form_submit_button("💾 খরচ সেভ করুন", type="primary"):
            if exp_category is None:
                st.warning("দয়া করে আগে একটি খরচের খাত নির্বাচন করুন।")
            elif exp_amount <= 0:
                st.warning("দয়া করে খরচের টাকার পরিমাণ লিখুন।")
            else:
                st.session_state.daily_expenses.append({
                    "তারিখ": exp_date.strftime("%d-%m-%Y"),
                    "খাত": exp_category,
                    "বিবরণ": exp_note.strip() if exp_note.strip() else "-",
                    "টাকা": exp_amount
                })
                st.success(f"✅ {exp_category} বাবদ {exp_amount:,} ৳ খরচ সফলভাবে সেভ হয়েছে!")
                st.rerun()

    if st.session_state.daily_expenses:
        st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)
        st.markdown("#### 📋 দৈনিক খরচের তালিকা")
        for idx in range(len(st.session_state.daily_expenses) - 1, -1, -1):
            row = st.session_state.daily_expenses[idx]
            with st.container(border=True):
                c_txt, c_amt, c_del = st.columns([3.8, 1.2, 0.7], gap="small")
                with c_txt:
                    st.markdown(
                        f"<div style='font-size:16px; font-weight:700; color:#0f172a;'>{idx + 1}. {row['খাত']}</div>"
                        f"<div style='font-size:13px; color:#64748b;'>📝 বিবরণ: {row['বিবরণ']} • 📅 {row['তারিখ']}</div>",
                        unsafe_allow_html=True
                    )
                with c_amt:
                    st.markdown(
                        f"<div style='font-size:18px; font-weight:700; color:#dc2626; text-align:right; padding-top:6px;'>− {row['টাকা']:,} ৳</div>",
                        unsafe_allow_html=True
                    )
                with c_del:
                    if st.button("🗑️", key=f"del_daily_exp_{idx}", help="ভুল এন্ট্রি মুছুন", use_container_width=True):
                        st.session_state.daily_expenses.pop(idx)
                        st.rerun()
    else:
        st.info("এখনো কোনো দৈনিক খরচের এন্ট্রি দেওয়া হয়নি।")

# ==================== ৬. 👷 কর্মচারীর বেতন (পাসওয়ার্ড সুরক্ষিত ডিলিটসহ) ====================
elif selected_menu == "👷 কর্মচারীর বেতন":
    st.markdown("### 👷 কর্মচারীর বেতন প্রদান ও অবশিষ্ট পাওনা হিসাব")

    if not st.session_state.staff_master:
        st.warning("কোনো কর্মচারীর তথ্য যোগ করা নেই। বাম পাশের মেনু থেকে '⚙️ সেটিংস -> 📋 কর্মচারীর বিবরণী'-তে গিয়ে আগে কর্মচারীর নাম ও বেতন যোগ করুন।")
    else:
        sc1, sc2, sc3 = st.columns(3)
        with sc1:
            st.markdown(
                f"""
                <div class="glass-stat-card">
                    <div class="stat-label">📋 মাসিক মোট নির্ধারিত বেতন</div>
                    <div class="stat-value" style="color: #0066ff;">{total_staff_monthly_budget:,} ৳</div>
                    <div class="stat-sub">মোট কর্মচারী: <b>{len(st.session_state.staff_master)} জন</b></div>
                </div>
                """,
                unsafe_allow_html=True
            )
        with sc2:
            st.markdown(
                f"""
                <div class="glass-stat-card">
                    <div class="stat-label">💸 মোট পরিশোধিত (কর্তন)</div>
                    <div class="stat-value" style="color: #059669;">{total_staff_paid:,} ৳</div>
                    <div class="stat-sub">মোট লেনদেন: <b>{len(st.session_state.staff_salary_payments)} বার</b></div>
                </div>
                """,
                unsafe_allow_html=True
            )
        with sc3:
            rem_color = "#dc2626" if remaining_staff_salary > 0 else "#059669"
            st.markdown(
                f"""
                <div class="glass-stat-card">
                    <div class="stat-label">⏳ মাসের অবশিষ্ট পাওনা বেতন</div>
                    <div class="stat-value" style="color: {rem_color};">{remaining_staff_salary:,} ৳</div>
                    <div class="stat-sub">নির্ধারিত বেতন থেকে পরিশোধিত টাকা বিয়োগ করে</div>
                </div>
                """,
                unsafe_allow_html=True
            )

        st.markdown("<div style='height: 16px;'></div>", unsafe_allow_html=True)

        for s_item in st.session_state.staff_master:
            s_nm = s_item["নাম"]
            s_fixed = s_item["মাসিক_বেতন"]
            s_paid_ind = sum(p["টাকা"] for p in st.session_state.staff_salary_payments if p["কর্মচারী"] == s_nm)
            s_rem_ind = max(0, s_fixed - s_paid_ind)
            with st.container(border=True):
                st.markdown(
                    f"<div style='display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:8px;'>"
                    f"<div><b style='font-size:17px; color:#0f172a;'>👤 {s_nm}</b> <span style='font-size:13px; color:#64748b;'>({s_item.get('বিবরণ', '')} • 📞 {s_item.get('ফোন', '')})</span></div>"
                    f"<div style='font-size:14.5px;'>মাসিক: <b>{s_fixed:,} ৳</b> • পরিশোধিত: <b style='color:#059669;'>{s_paid_ind:,} ৳</b> • অবশিষ্ট বাকি: <b style='color:#dc2626;'>{s_rem_ind:,} ৳</b></div>"
                    f"</div>",
                    unsafe_allow_html=True
                )

        st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)

        with st.container(border=True):
            st.markdown("#### 💵 আজকের / নির্দিষ্ট তারিখের বেতন প্রদান করুন")
            staff_names_list = [s["নাম"] for s in st.session_state.staff_master]
            with st.form("staff_salary_pay_form", clear_on_submit=True):
                sp1, sp2, sp3, sp4 = st.columns([1.2, 1.3, 1.1, 1.6])
                pay_date = sp1.date_input("তারিখ", value=date.today(), key="staff_pay_date")
                selected_staff = sp2.selectbox("কর্মচারীর নাম", staff_names_list, key="staff_pay_person")
                pay_amount = sp3.number_input("প্রদত্ত টাকা (৳)", min_value=0, step=100, key="staff_pay_amt")
                pay_note = sp4.text_input("মন্তব্য / নোট (ঐচ্ছিক)", placeholder="যেমন: হাতখরচ বা দৈনিক বেতন বাবদ", key="staff_pay_note")

                if st.form_submit_button("✅ বেতন প্রদান সেভ করুন", type="primary"):
                    if pay_amount > 0:
                        target_staff_obj = next((s for s in st.session_state.staff_master if s["নাম"] == selected_staff), None)
                        fixed_s_amt = target_staff_obj["মাসিক_বেতন"] if target_staff_obj else 0
                        prev_paid = sum(p["টাকা"] for p in st.session_state.staff_salary_payments if p["কর্মচারী"] == selected_staff)
                        new_rem = max(0, fixed_s_amt - (prev_paid + pay_amount))

                        st.session_state.staff_salary_payments.append({
                            "তারিখ": pay_date.strftime("%d-%m-%Y"),
                            "কর্মচারী": selected_staff,
                            "টাকা": pay_amount,
                            "অবশিষ্ট_ছিল": new_rem,
                            "নোট": pay_note.strip() if pay_note.strip() else "দৈনিক বেতন প্রদান"
                        })
                        st.success(f"✅ {selected_staff}-কে {pay_amount:,} ৳ বেতন প্রদান সফল হয়েছে! বর্তমানে অবশিষ্ট বেতন: {new_rem:,} ৳")
                        st.rerun()
                    else:
                        st.warning("দয়া করে টাকার পরিমাণ লিখুন।")

        if st.session_state.pending_salary_del_idx is not None:
            del_i = st.session_state.pending_salary_del_idx
            if 0 <= del_i < len(st.session_state.staff_salary_payments):
                target_pay = st.session_state.staff_salary_payments[del_i]
                with st.container(border=True):
                    st.error(
                        f"🔐 **সুরক্ষা যাচাই:** আপনি **{target_pay['কর্মচারী']}**-এর **{target_pay['তারিখ']}** তারিখের "
                        f"**{target_pay['টাকা']:,} ৳** বেতনের এন্ট্রিটি মুছতে চাইছেন। এটি মুছতে আপনার গোপন অ্যাডমিন পাসওয়ার্ড দিন:"
                    )
                    with st.form("verify_salary_delete_pin_form"):
                        pin_col1, pin_col2, pin_col3 = st.columns([2.0, 1.3, 1.0])
                        entered_pin = pin_col1.text_input("অ্যাডমিন পাসওয়ার্ড লিখুন", type="password", placeholder="••••••", label_visibility="collapsed")
                        if pin_col2.form_submit_button("🔓 পাসওয়ার্ড দিয়ে মুছুন", type="primary", use_container_width=True):
                            if entered_pin == st.session_state.admin_delete_pin:
                                st.session_state.staff_salary_payments.pop(del_i)
                                st.session_state.pending_salary_del_idx = None
                                st.success("✅ সঠিক পাসওয়ার্ড! বেতনের এন্ট্রিটি সফলভাবে মুছে ফেলা হয়েছে।")
                                st.rerun()
                            else:
                                st.warning("❌ ভুল পাসওয়ার্ড! আপনি এটি ডিলিট করার অনুমতিপ্রাপ্ত নন।")
                        if pin_col3.form_submit_button("বাতিল", use_container_width=True):
                            st.session_state.pending_salary_del_idx = None
                            st.rerun()

        if st.session_state.staff_salary_payments:
            st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)
            st.markdown("#### 📜 বেতন প্রদানের তালিকা (সর্বশেষ লেনদেন উপরে)")
            for p_idx in range(len(st.session_state.staff_salary_payments) - 1, -1, -1):
                p_row = st.session_state.staff_salary_payments[p_idx]
                with st.container(border=True):
                    p_info, p_amt, p_del = st.columns([3.8, 1.4, 0.7], gap="small")
                    with p_info:
                        st.markdown(
                            f"<div style='font-size:15.5px; font-weight:700; color:#0f172a;'>{p_idx + 1}. 👤 {p_row['কর্মচারী']} • 📅 তারিখ: {p_row['তারিখ']}</div>"
                            f"<div style='font-size:13px; color:#64748b;'>📝 {p_row['নোট']} • এই লেনদেনের পর অবশিষ্ট পাওনা: <b>{p_row['অবশিষ্ট_ছিল']:,} ৳</b></div>",
                            unsafe_allow_html=True
                        )
                    with p_amt:
                        st.markdown(
                            f"<div style='font-size:17px; font-weight:700; color:#dc2626; text-align:right; padding-top:6px;'>− {p_row['টাকা']:,} ৳</div>",
                            unsafe_allow_html=True
                        )
                    with p_del:
                        if st.button("🔒 🗑️", key=f"del_staff_pay_{p_idx}", help="পাসওয়ার্ড দিয়ে এন্ট্রি মুছুন", use_container_width=True):
                            st.session_state.pending_salary_del_idx = p_idx
                            st.rerun()
        else:
            st.info(f"এখন পর্যন্ত কোনো বেতন প্রদান করা হয়নি। সম্পূর্ণ {total_staff_monthly_budget:,} ৳ অবশিষ্ট রয়েছে।")

# ==================== ৭. ⚙️ সেটিংস ====================
elif selected_menu == "⚙️ সেটিংস":
    set_tabs = [
        ("➕ নতুন গাড়ি যোগ", "add_car"),
        ("📝 ড্রাইভার তালিকা সংশোধনী", "manage_drivers"),
        ("🛠️ জমা আদায় মেরামত", "repair_joma"),
        ("📋 কর্মচারীর বিবরণী", "staff_details")
    ]

    nav_col, _ = st.columns([1.8, 2.2])
    with nav_col:
        for s_label, s_mode in set_tabs:
            is_s_active = (st.session_state.settings_mode == s_mode)
            if st.button(
                s_label,
                key=f"set_sub_btn_{s_mode}",
                type="primary" if is_s_active else "secondary",
                use_container_width=True
            ):
                st.session_state.settings_mode = s_mode
                st.rerun()

    st.divider()

    # --- অপশন ১: নতুন গাড়ি যোগ ---
    if st.session_state.settings_mode == "add_car":
        st.markdown("### ➕ নতুন গাড়ি যোগ")

        sel_c1, sel_c2, _ = st.columns([1.3, 1.5, 2.0], gap="small")
        with sel_c1:
            driver_type = st.selectbox(
                "হিসাবের খাত নির্বাচন করুন",
                ["নিজস্ব গাড়ি", "চার্জের গাড়ি (বাহিরের গাড়ি)"],
                key="settings_add_car_type"
            )
            actual_type = "নিজস্ব গাড়ি" if driver_type == "নিজস্ব গাড়ি" else "চার্জের গাড়ি"

        with sel_c2:
            def update_model_defaults():
                m_sel = st.session_state.get("settings_vehicle_model", "মিশুক গাড়ি (৪ ব্যাটারি)")
                st.session_state.new_car_model_sel = m_sel

            vehicle_model = st.selectbox(
                "গাড়ির ধরন (মিশুক / ইজি বাইক / কভার ভ্যান)",
                [
                    "মিশুক গাড়ি (৪ ব্যাটারি)",
                    "ইজি বাইক (৫ ব্যাটারি)",
                    "কভার ভ্যান"
                ],
                key="settings_vehicle_model",
                on_change=update_model_defaults
            )

        cur_selected_model = st.session_state.get("new_car_model_sel", vehicle_model)

        if cur_selected_model == "মিশুক গাড়ি (৪ ব্যাটারি)":
            default_charge_val = 170
            default_rent_val = 50
            default_hourly_val = 30
        elif cur_selected_model == "ইজি বাইক (৫ ব্যাটারি)":
            default_charge_val = 200
            default_rent_val = 50
            default_hourly_val = 40
        else:
            default_charge_val = 200
            default_rent_val = 50
            default_hourly_val = 30

        with st.form("add_new_driver_settings", clear_on_submit=True):
            nd1, nd2, nd3 = st.columns(3)
            driver_name = nd1.text_input("চালকের নাম", placeholder="চালকের নাম লিখুন", key="settings_driver_name")
            driver_addr = nd2.text_input("ঠিকানা", placeholder="গ্রামের নাম / এলাকা", key="settings_driver_addr")
            driver_phone = nd3.text_input("ফোন নাম্বার", placeholder="017XX-XXXXXX", key="settings_driver_phone")

            if actual_type == "নিজস্ব গাড়ি":
                fixed_joma_input = st.number_input("দৈনিক জমা (৳)", min_value=0, value=470, step=10, key="settings_joma")
                fixed_charge_input = 0
                fixed_rent_input = 0
                hourly_charge_input = 0
            else:
                c_in1, c_in2, c_in3 = st.columns(3)
                fixed_charge_input = c_in1.number_input(
                    "রাতের চার্জ বিল (৳)",
                    min_value=0,
                    value=default_charge_val,
                    step=10,
                    key=f"settings_charge_{cur_selected_model}"
                )
                fixed_rent_input = c_in2.number_input(
                    "ঘর ভাড়া (৳)",
                    min_value=0,
                    value=default_rent_val,
                    step=10,
                    key=f"settings_rent_{cur_selected_model}"
                )
                hourly_charge_input = c_in3.number_input(
                    "দিনের প্রতি ঘণ্টা চার্জ (৳)",
                    min_value=0,
                    value=default_hourly_val,
                    step=5,
                    key=f"settings_hourly_{cur_selected_model}"
                )
                fixed_joma_input = 0

            if st.form_submit_button("✅ নতুন গাড়ি সেভ করুন", type="primary"):
                if driver_name.strip():
                    st.session_state.drivers_master.append({
                        "নাম": driver_name.strip(),
                        "ঠিকানা": driver_addr.strip(),
                        "ফোন": driver_phone.strip(),
                        "ধরন": actual_type,
                        "গাড়ির_মডেল": cur_selected_model,
                        "নির্ধারিত_জমা": fixed_joma_input,
                        "নির্ধারিত_চার্জ": fixed_charge_input,
                        "নির্ধারিত_ঘর_ভাড়া": fixed_rent_input,
                        "প্রতি_ঘণ্টা_চার্জ": hourly_charge_input
                    })
                    st.success(f"✅ {driver_name} ({cur_selected_model} • {actual_type}) সফলভাবে তালিকায় যুক্ত হয়েছে!")
                    st.rerun()

    # --- অপশন ২: ড্রাইভার তালিকা সংশোধনী ---
    elif st.session_state.settings_mode == "manage_drivers":
        st.markdown("### 📝 ড্রাইভার তালিকা সংশোধনী")
        st.caption("যেকোনো চালকের নাম, গাড়ির ধরন, ঠিকানা, ফোন নাম্বার বা চার্জ পরিবর্তন করতে 'এডিট' বাটনে চাপুন, এবং নাম মুছতে চাইলে দুইবার কনফার্মেশন দিন।")

        if st.session_state.edit_target is not None:
            edit_idx = st.session_state.edit_target
            if 0 <= edit_idx < len(st.session_state.drivers_master):
                d_edit = st.session_state.drivers_master[edit_idx]
                old_name = d_edit["নাম"]
                model_options = [
                    "মিশুক গাড়ি (৪ ব্যাটারি)",
                    "ইজি বাইক (৫ ব্যাটারি)",
                    "কভার ভ্যান"
                ]
                cur_model = d_edit.get("গাড়ির_মডেল", "মিশুক গাড়ি (৪ ব্যাটারি)")
                cur_model_idx = model_options.index(cur_model) if cur_model in model_options else 0

                with st.container(border=True):
                    st.info(f"✏️ **{old_name}**-এর তথ্য সংশোধন করছেন:")
                    with st.form("edit_driver_form"):
                        ec1, ec2, ec3, ec_mod = st.columns(4)
                        new_name = ec1.text_input("চালকের নাম", value=d_edit["নাম"], key="edit_name_input")
                        new_addr = ec2.text_input("ঠিকানা", value=d_edit["ঠিকানা"], key="edit_addr_input")
                        new_phone = ec3.text_input("ফোন নাম্বার", value=d_edit.get("ফোন", ""), key="edit_phone_input")
                        new_model = ec_mod.selectbox("গাড়ির ধরন", model_options, index=cur_model_idx, key="edit_model_input")

                        if d_edit["ধরন"] == "নিজস্ব গাড়ি":
                            new_joma = st.number_input("দৈনিক জমা (৳)", min_value=0, value=int(d_edit["নির্ধারিত_জমা"]), step=10, key="edit_joma_input")
                            new_charge = 0
                            new_rent = 0
                            new_hourly = 0
                        else:
                            ec4, ec5, ec6 = st.columns(3)
                            new_charge = ec4.number_input("রাতের চার্জ বিল (৳)", min_value=0, value=int(d_edit["নির্ধারিত_চার্জ"]), step=10, key="edit_charge_input")
                            new_rent = ec5.number_input("ঘর ভাড়া (৳)", min_value=0, value=int(d_edit["নির্ধারিত_ঘর_ভাড়া"]), step=10, key="edit_rent_input")
                            new_hourly = ec6.number_input("দিনের প্রতি ঘণ্টা চার্জ (৳)", min_value=0, value=int(d_edit.get("প্রতি_ঘণ্টা_চার্জ", 30)), step=5, key="edit_hourly_input")
                            new_joma = 0

                        b_save, b_cancel, _ = st.columns([1.4, 1.1, 2.5])
                        if b_save.form_submit_button("✅ সংশোধন সেভ করুন", type="primary", use_container_width=True):
                            if new_name.strip():
                                cleaned_name = new_name.strip()
                                st.session_state.drivers_master[edit_idx]["নাম"] = cleaned_name
                                st.session_state.drivers_master[edit_idx]["ঠিকানা"] = new_addr.strip()
                                st.session_state.drivers_master[edit_idx]["ফোন"] = new_phone.strip()
                                st.session_state.drivers_master[edit_idx]["গাড়ির_মডেল"] = new_model
                                st.session_state.drivers_master[edit_idx]["নির্ধারিত_জমা"] = new_joma
                                st.session_state.drivers_master[edit_idx]["নির্ধারিত_চার্জ"] = new_charge
                                st.session_state.drivers_master[edit_idx]["নির্ধারিত_ঘর_ভাড়া"] = new_rent
                                st.session_state.drivers_master[edit_idx]["প্রতি_ঘণ্টা_চার্জ"] = new_hourly

                                for row in st.session_state.own_cars:
                                    if row["চালক"] == old_name:
                                        row["চালক"] = cleaned_name
                                for row in st.session_state.charging_data:
                                    if row["চালক"] == old_name:
                                        row["চালক"] = cleaned_name
                                for row in st.session_state.due_recovery:
                                    if row["চালক"] == old_name:
                                        row["চালক"] = cleaned_name

                                st.session_state.edit_target = None
                                st.rerun()

                        if b_cancel.form_submit_button("বাতিল করুন", use_container_width=True):
                            st.session_state.edit_target = None
                            st.rerun()

        if st.session_state.delete_target is not None:
            target_name = st.session_state.delete_target
            with st.container(border=True):
                if st.session_state.delete_step == 1:
                    st.warning(f"⚠️ **১ম কনফার্মেশন:** আপনি কি নিশ্চিতভাবে **{target_name}**-কে চালকের তালিকা থেকে মুছে ফেলতে চান?")
                    c_yes1, c_no1, _ = st.columns([1.4, 1.1, 2.8])
                    if c_yes1.button("হ্যাঁ, ১ম বার নিশ্চিত করছি", key="confirm_del_1", type="primary", use_container_width=True):
                        st.session_state.delete_step = 2
                        st.rerun()
                    if c_no1.button("বাতিল করুন", key="cancel_del_1", use_container_width=True):
                        st.session_state.delete_target = None
                        st.session_state.delete_step = 0
                        st.rerun()

                elif st.session_state.delete_step == 2:
                    st.error(f"🚨 **২য় ও চূড়ান্ত কনফার্মেশন:** আপনি কি সত্যিই **{target_name}**-এর নাম স্থায়ীভাবে মুছে ফেলতে চান? একবার মুছলে আর ফিরে পাওয়া যাবে না!")
                    c_yes2, c_no2, _ = st.columns([1.6, 1.1, 2.6])
                    if c_yes2.button("হ্যাঁ, চূড়ান্তভাবে মুছে ফেলুন", key="confirm_del_2", type="primary", use_container_width=True):
                        st.session_state.drivers_master = [
                            d for d in st.session_state.drivers_master if d["নাম"] != target_name
                        ]
                        st.session_state.delete_target = None
                        st.session_state.delete_step = 0
                        st.success(f"{target_name}-এর নাম তালিকা থেকে সফলভাবে মুছে ফেলা হয়েছে।")
                        st.rerun()
                    if c_no2.button("না, ফিরে যান", key="cancel_del_2", use_container_width=True):
                        st.session_state.delete_target = None
                        st.session_state.delete_step = 0
                        st.rerun()

        st.markdown("<div style='height: 6px;'></div>", unsafe_allow_html=True)

        if not st.session_state.drivers_master:
            st.info("তালিকায় কোনো চালক নেই।")
        else:
            st.markdown("#### 🚙 নিজস্ব গাড়ির চালকবৃন্দ")
            own_count = 0
            for master_idx, d in enumerate(st.session_state.drivers_master):
                if d["ধরন"] == "নিজস্ব গাড়ি":
                    own_count += 1
                    ph = f" • 📞 {d.get('ফোন', '')}" if d.get("ফোন") else ""
                    v_mod = d.get("গাড়ির_মডেল", "ইজি বাইক (৫ ব্যাটারি)")
                    with st.container(border=True):
                        col_info, col_edit, col_del = st.columns([3.8, 1.0, 1.0], gap="small")
                        with col_info:
                            st.markdown(
                                f"<div style='font-size:16.5px; font-weight:700; color:#0f172a;'>{own_count}. {d['নাম']} <span style='font-size:13px; color:#0066ff; font-weight:600;'>({v_mod})</span></div>"
                                f"<div style='font-size:13px; color:#64748b;'>📍 {d['ঠিকানা']}{ph} • দৈনিক জমা: {d['নির্ধারিত_জমা']} ৳</div>",
                                unsafe_allow_html=True
                            )
                        if col_edit.button("✏️ এডিট", key=f"edit_btn_own_{master_idx}", use_container_width=True):
                            st.session_state.edit_target = master_idx
                            st.session_state.delete_target = None
                            st.rerun()
                        if col_del.button("🗑️ মুছুন", key=f"del_btn_own_{master_idx}", use_container_width=True):
                            st.session_state.delete_target = d["নাম"]
                            st.session_state.delete_step = 1
                            st.session_state.edit_target = None
                            st.rerun()

            st.markdown("<div style='height: 12px;'></div>", unsafe_allow_html=True)
            st.markdown("#### ⚡ চার্জের গাড়ির চালকবৃন্দ")
            chg_count = 0
            for master_idx, d in enumerate(st.session_state.drivers_master):
                if d["ধরন"] == "চার্জের গাড়ি":
                    chg_count += 1
                    ph = f" • 📞 {d.get('ফোন', '')}" if d.get("ফোন") else ""
                    hr_rate = d.get("প্রতি_ঘণ্টা_চার্জ", 30)
                    v_mod = d.get("গাড়ির_মডেল", "মিশুক গাড়ি (৪ ব্যাটারি)")
                    with st.container(border=True):
                        col_info, col_edit, col_del = st.columns([3.8, 1.0, 1.0], gap="small")
                        with col_info:
                            st.markdown(
                                f"<div style='font-size:16.5px; font-weight:700; color:#0f172a;'>{chg_count}. {d['নাম']} <span style='font-size:13px; color:#0066ff; font-weight:600;'>({v_mod})</span></div>"
                                f"<div style='font-size:13px; color:#64748b;'>📍 {d['ঠিকানা']}{ph} • চার্জ: {d['নির্ধারিত_চার্জ']} ৳ • ঘণ্টা: {hr_rate} ৳ • ঘর ভাড়া: {d['নির্ধারিত_ঘর_ভাড়া']} ৳</div>",
                                unsafe_allow_html=True
                            )
                        if col_edit.button("✏️ এডিট", key=f"edit_btn_chg_{master_idx}", use_container_width=True):
                            st.session_state.edit_target = master_idx
                            st.session_state.delete_target = None
                            st.rerun()
                        if col_del.button("🗑️ মুছুন", key=f"del_btn_chg_{master_idx}", use_container_width=True):
                            st.session_state.delete_target = d["নাম"]
                            st.session_state.delete_step = 1
                            st.session_state.edit_target = None
                            st.rerun()

    # --- অপশন ৩: জমা আদায় মেরামত ---
    elif st.session_state.settings_mode == "repair_joma":
        st.markdown("### 🛠️ বিগত দিনের জমা আদায় মেরামত বা সংশোধন")
        st.caption("কয়েক দিন আগের (যেমন: ২-৩ দিন বা ৬-৭ দিন আগের) ভুল জমা বা বকেয়া এন্ট্রি সরাসরি নির্দিষ্ট তারিখ সিলেক্ট করে সংশোধন করুন।")

        all_driver_names = [d["নাম"] for d in (own_drivers + charge_drivers)]
        if not all_driver_names:
            st.warning("চালকের তালিকায় কোনো ড্রাইভার নেই।")
        else:
            with st.form("repair_joma_form", clear_on_submit=True):
                r_col1, r_col2 = st.columns(2)
                repair_date = r_col1.date_input("সংশোধনের জন্য সঠিক তারিখ নির্বাচন করুন", value=date.today())
                repair_driver = r_col2.selectbox("চালকের নাম নির্বাচন করুন", all_driver_names)

                r_col3, r_col4, r_col5 = st.columns(3)
                repair_category = r_col3.selectbox("হিসাবের খাত", [
                    "নিজস্ব গাড়ির জমা",
                    "চার্জের বিল",
                    "ঘর ভাড়া"
                ])
                repair_action = r_col4.selectbox("অবস্থা", ["আদায়", "বাকি"])
                repair_amount = r_col5.number_input("সঠিক টাকার পরিমাণ (৳)", min_value=0, step=10)
                repair_note = st.text_input("মেরামতের কারণ / নোট (ঐচ্ছিক)", placeholder="যেমন: গত রবিবারের এন্ট্রি ভুল সংশোধন")

                if st.form_submit_button("🛠️ মেরামত রেকর্ড সেভ করুন", type="primary"):
                    if repair_amount > 0:
                        st.session_state.repair_records.append({
                            "তারিখ": repair_date.strftime("%d-%m-%Y"),
                            "চালক": repair_driver,
                            "খাত": repair_category,
                            "ধরণ": repair_action,
                            "টাকা": repair_amount,
                            "নোট": repair_note.strip() if repair_note.strip() else "-"
                        })
                        st.success(f"✅ {repair_date.strftime('%d-%m-%Y')} তারিখের জন্য {repair_driver}-এর হিসাব সফলভাবে মেরামত করা হয়েছে!")
                        st.rerun()
                    else:
                        st.warning("দয়া করে টাকার পরিমাণ লিখুন।")

        if st.session_state.repair_records:
            st.markdown("<div style='height: 12px;'></div>", unsafe_allow_html=True)
            st.markdown("#### 📋 বিগত দিনের মেরামতের তালিকা")
            for r_idx in range(len(st.session_state.repair_records) - 1, -1, -1):
                rec = st.session_state.repair_records[r_idx]
                with st.container(border=True):
                    rc_info, rc_del = st.columns([5, 1])
                    with rc_info:
                        st.markdown(
                            f"<div style='font-size:15px; font-weight:700; color:#0f172a;'>📅 তারিখ: {rec['তারিখ']} • 🚙 {rec['চালক']} ({rec['খাত']})</div>"
                            f"<div style='font-size:13px; color:#64748b;'>অবস্থা: <b>{rec['ধরণ']}</b> • টাকা: <b style='color:#059669;'>{rec['টাকা']} ৳</b> • নোট: {rec['নোট']}</div>",
                            unsafe_allow_html=True
                        )
                    with rc_del:
                        if st.button("🗑️", key=f"del_repair_{r_idx}", help="এই মেরামত রেকর্ড মুছুন", use_container_width=True):
                            st.session_state.repair_records.pop(r_idx)
                            st.rerun()

    # --- অপশন ৪: 📋 কর্মচারীর বিবরণী ---
    elif st.session_state.settings_mode == "staff_details":
        st.markdown("### 📋 কর্মচারীর বিবরণী ও মাসিক বেতন নির্ধারণ")
        st.caption("এখান থেকে কর্মচারীর নাম, ঠিকানা, ফোন নাম্বার, বিস্তারিত বিবরণ এবং মাসিক নির্ধারিত বেতন যোগ বা সংশোধন করুন।")

        with st.form("add_new_staff_form", clear_on_submit=True):
            st1, st2, st3 = st.columns(3)
            s_name_in = st1.text_input("কর্মচারীর নাম", placeholder="কর্মচারীর পুরো নাম লিখুন")
            s_addr_in = st2.text_input("ঠিকানা", placeholder="গ্রামের নাম / এলাকা")
            s_phone_in = st3.text_input("ফোন নাম্বার", placeholder="017XX-XXXXXX")

            st4, st5 = st.columns([1.2, 2.3])
            s_salary_in = st4.number_input("মাসিক নির্ধারিত বেতন (৳)", min_value=0, value=20000, step=500)
            s_info_in = st5.text_input("বিস্তারিত তথ্য / পদবি", placeholder="যেমন: রাতের ডিউটি ও চার্জিং মনিটরিং")

            if st.form_submit_button("✅ কর্মচারীর তথ্য সেভ করুন", type="primary"):
                if s_name_in.strip():
                    st.session_state.staff_master.append({
                        "নাম": s_name_in.strip(),
                        "ঠিকানা": s_addr_in.strip() if s_addr_in.strip() else "-",
                        "ফোন": s_phone_in.strip() if s_phone_in.strip() else "-",
                        "মাসিক_বেতন": s_salary_in,
                        "বিবরণ": s_info_in.strip() if s_info_in.strip() else "-"
                    })
                    st.success(f"✅ {s_name_in} সফলভাবে কর্মচারী তালিকায় যুক্ত হয়েছে!")
                    st.rerun()
                else:
                    st.warning("দয়া করে কর্মচারীর নাম লিখুন।")

        if st.session_state.edit_staff_target is not None:
            e_s_idx = st.session_state.edit_staff_target
            if 0 <= e_s_idx < len(st.session_state.staff_master):
                s_ed = st.session_state.staff_master[e_s_idx]
                old_s_name = s_ed["নাম"]
                with st.container(border=True):
                    st.info(f"✏️ **{old_s_name}**-এর বিবরণী সংশোধন করছেন:")
                    with st.form("edit_staff_detail_form"):
                        es1, es2, es3 = st.columns(3)
                        ed_s_name = es1.text_input("কর্মচারীর নাম", value=s_ed["নাম"])
                        ed_s_addr = es2.text_input("ঠিকানা", value=s_ed["ঠিকানা"])
                        ed_s_phone = es3.text_input("ফোন নাম্বার", value=s_ed["ফোন"])

                        es4, es5 = st.columns([1.2, 2.3])
                        ed_s_sal = es4.number_input("মাসিক নির্ধারিত বেতন (৳)", min_value=0, value=int(s_ed["মাসিক_বেতন"]), step=500)
                        ed_s_desc = es5.text_input("বিস্তারিত তথ্য / পদবি", value=s_ed.get("বিবরণ", ""))

                        sb1, sb2, _ = st.columns([1.4, 1.1, 2.5])
                        if sb1.form_submit_button("✅ সংশোধন সেভ করুন", type="primary", use_container_width=True):
                            if ed_s_name.strip():
                                clean_s_nm = ed_s_name.strip()
                                st.session_state.staff_master[e_s_idx] = {
                                    "নাম": clean_s_nm,
                                    "ঠিকানা": ed_s_addr.strip(),
                                    "ফোন": ed_s_phone.strip(),
                                    "মাসিক_বেতন": ed_s_sal,
                                    "বিবরণ": ed_s_desc.strip()
                                }
                                for p_item in st.session_state.staff_salary_payments:
                                    if p_item["কর্মচারী"] == old_s_name:
                                        p_item["কর্মচারী"] = clean_s_nm
                                st.session_state.edit_staff_target = None
                                st.rerun()
                        if sb2.form_submit_button("বাতিল করুন", use_container_width=True):
                            st.session_state.edit_staff_target = None
                            st.rerun()

        if st.session_state.pending_staff_del_idx is not None:
            st_del_i = st.session_state.pending_staff_del_idx
            if 0 <= st_del_i < len(st.session_state.staff_master):
                target_stf = st.session_state.staff_master[st_del_i]
                with st.container(border=True):
                    st.error(
                        f"🔐 **সুরক্ষা যাচাই:** আপনি কর্মচারী **{target_stf['নাম']}**-এর তথ্য স্থায়ীভাবে মুছতে চাইছেন। "
                        f"এটি ডিলিট করতে আপনার অ্যাডমিন পাসওয়ার্ড দিন:"
                    )
                    with st.form("verify_staff_master_delete_form"):
                        sp_c1, sp_c2, sp_c3 = st.columns([2.0, 1.3, 1.0])
                        entered_stf_pin = sp_c1.text_input("অ্যাডমিন পাসওয়ার্ড লিখুন", type="password", placeholder="••••••", label_visibility="collapsed")
                        if sp_c2.form_submit_button("🔓 পাসওয়ার্ড দিয়ে মুছুন", type="primary", use_container_width=True):
                            if entered_stf_pin == st.session_state.admin_delete_pin:
                                st.session_state.staff_master.pop(st_del_i)
                                st.session_state.pending_staff_del_idx = None
                                st.success("✅ কর্মচারীর তথ্য সফলভাবে মুছে ফেলা হয়েছে।")
                                st.rerun()
                            else:
                                st.warning("❌ ভুল পাসওয়ার্ড! আপনি এটি ডিলিট করার অনুমতিপ্রাপ্ত নন।")
                        if sp_c3.form_submit_button("বাতিল", use_container_width=True):
                            st.session_state.pending_staff_del_idx = None
                            st.rerun()

        st.markdown("<div style='height: 12px;'></div>", unsafe_allow_html=True)
        st.markdown("#### 👥 নিবন্ধিত কর্মচারীদের তালিকা")

        if not st.session_state.staff_master:
            st.info("এখনো কোনো কর্মচারীর বিবরণী যোগ করা হয়নি।")
        else:
            for s_idx, stf in enumerate(st.session_state.staff_master):
                with st.container(border=True):
                    sc_info, sc_edit, sc_del = st.columns([3.8, 1.0, 1.0], gap="small")
                    with sc_info:
                        st.markdown(
                            f"<div style='font-size:17px; font-weight:700; color:#0f172a;'>{s_idx + 1}. {stf['নাম']} "
                            f"<span style='font-size:13.5px; color:#0066ff; font-weight:700;'>(মাসিক বেতন: {stf['মাসিক_বেতন']:,} ৳)</span></div>"
                            f"<div style='font-size:13px; color:#64748b;'>📍 {stf['ঠিকানা']} • 📞 {stf['ফোন']} • 📝 {stf.get('বিবরণ', '-')}</div>",
                            unsafe_allow_html=True
                        )
                    if sc_edit.button("✏️ এডিট", key=f"ed_staff_btn_{s_idx}", use_container_width=True):
                        st.session_state.edit_staff_target = s_idx
                        st.session_state.pending_staff_del_idx = None
                        st.rerun()
                    if sc_del.button("🔒 মুছুন", key=f"del_staff_btn_{s_idx}", help="পাসওয়ার্ড দিয়ে মুছুন", use_container_width=True):
                        st.session_state.pending_staff_del_idx = s_idx
                        st.session_state.edit_staff_target = None
                        st.rerun()

        st.markdown("<div style='height: 16px;'></div>", unsafe_allow_html=True)
        with st.expander("🔐 অ্যাডমিন ডিলিট পাসওয়ার্ড পরিবর্তন করুন"):
            with st.form("change_admin_pin_form", clear_on_submit=True):
                pc1, pc2, pc3 = st.columns(3)
                old_pin_in = pc1.text_input("বর্তমান পাসওয়ার্ড", type="password", placeholder="বর্তমান পাসওয়ার্ড")
                new_pin_in = pc2.text_input("নতুন পাসওয়ার্ড", type="password", placeholder="নতুন পাসওয়ার্ড লিখুন")
                conf_pin_in = pc3.text_input("নতুন পাসওয়ার্ড নিশ্চিত করুন", type="password", placeholder="আবার লিখুন")

                if st.form_submit_button("🔑 পাসওয়ার্ড আপডেট করুন", type="primary"):
                    if old_pin_in != st.session_state.admin_delete_pin:
                        st.error("❌ বর্তমান পাসওয়ার্ডটি সঠিক নয়!")
                    elif len(new_pin_in.strip()) < 4:
                        st.warning("⚠️ নতুন পাসওয়ার্ড কমপক্ষে ৪ অক্ষরের হতে হবে।")
                    elif new_pin_in != conf_pin_in:
                        st.error("❌ নতুন পাসওয়ার্ড দুটি মেলেনি!")
                    else:
                        st.session_state.admin_delete_pin = new_pin_in.strip()
                        st.success("✅ আপনার গোপন অ্যাডমিন পাসওয়ার্ড সফলভাবে পরিবর্তন করা হয়েছে!")