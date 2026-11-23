#!/usr/bin/env python3
"""Plain-English Nous Portal usage check for this account.

Run with the Hermes venv Python from anywhere:

    /opt/hermes/.venv/bin/python3 check_usage.py

It reads only this machine's own Hermes sign-in, and never prints tokens.
It cannot spend anything: it reports settings and warns.
"""
import sys

sys.path.insert(0, "/opt/hermes")
from hermes_cli import nous_account as na  # noqa: E402

WARN_AT = 80.0


def money(value):
    try:
        return f"${float(value):.2f}"
    except (TypeError, ValueError):
        return None


def field(obj, name, default=None):
    return getattr(obj, name, default) if obj is not None else default


def main():
    try:
        info = na.get_nous_portal_account_info(force_fresh=True)
    except Exception as exc:  # noqa: BLE001
        print(f"Could not reach Nous Portal right now ({type(exc).__name__}).")
        print("Your settings have not changed. Try again in a moment.")
        return 1

    if not info.logged_in:
        print("You are not signed in to Nous Portal on this machine.")
        print("Run: hermes portal login")
        return 1

    sub = info.subscription
    paid = info.paid_service_access_info
    win = info.usage_window

    plan = field(sub, "plan") or "Free tier"
    print(f"Plan: {plan}" + (f" (tier {field(sub, 'tier')})" if field(sub, "tier") else ""))
    if field(sub, "monthly_charge") is not None:
        print(f"Monthly charge: {money(field(sub, 'monthly_charge'))}")
    if field(sub, "current_period_end"):
        print(f"Renews: {str(field(sub, 'current_period_end'))[:10]}")
    if field(sub, "credits_remaining") is not None:
        print(f"Subscription credits left: {money(field(sub, 'credits_remaining'))}")
    if field(sub, "rollover_credits"):
        print(f"Rollover credits: {money(field(sub, 'rollover_credits'))}")
    if field(paid, "purchased_credits_remaining"):
        print(f"Purchased credits left: {money(field(paid, 'purchased_credits_remaining'))}")

    cap = field(paid, "member_spend_cap_usd")
    if cap is not None:
        line = f"Spend cap: {money(cap)}"
        left = field(paid, "member_spend_cap_remaining_usd")
        if left is not None:
            line += f" ({money(left)} remaining)"
        print(line)

    if win is not None:
        topup = field(win, "auto_top_up_enabled")
        print("Auto top-up: " + ("ON - extra credits can be bought for you automatically"
                                if topup else "OFF - nothing is ever bought automatically"))
        print("Keep going on credits: " + ("yes" if field(win, "keep_going_on_credits") else "no"))

        gauges = field(win, "gauges") or ()
        if gauges:
            print("Allowance used:")
            for g in gauges:
                bp = getattr(g, "used_bp", 0) or 0
                pct = round(bp / 100.0, 1)
                label = getattr(g, "label", None) or getattr(g, "id", "?")
                flag = "   <- running low" if pct >= WARN_AT else ""
                print(f"   {label}: {pct:.1f}%{flag}")
        else:
            print("No usage gauges published for this plan.")
    else:
        print("No usage window on this account (free tier or an older plan).")

    print()
    print("To keep a flat monthly bill: leave Auto top-up OFF.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
