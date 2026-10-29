"""Generated from the Public API document. Do not edit."""

CONTRACT_SHA256 = "718888ffd87ce0bd86537d3f9531fe9fbce07ac71e7be92351fecf39ce09052c"
"""SHA-256 of the Public API document this package was generated from."""

IDEMPOTENT_CREATES: tuple[str, ...] = (
    "/v1/allocation/rules",
    "/v1/annotations",
    "/v1/apps",
    "/v1/budgets",
    "/v1/business-metrics",
    "/v1/cost-alerts",
    "/v1/cost-estimates",
    "/v1/cost-report-subscriptions",
    "/v1/cost-reports",
    "/v1/custom-providers/{providerId}/costs",
    "/v1/dashboards",
    "/v1/dashboards/{dashboardId}/widgets",
    "/v1/folders",
    "/v1/providers",
    "/v1/saved-filters",
    "/v1/savings-views",
    "/v1/segments",
    "/v1/teams",
    "/v1/users",
    "/v1/virtual-tags",
    "/v1/workspace-providers",
    "/v1/workspaces",
)
"""The creates that take an Idempotency-Key; create_client sends a fresh one with each."""
