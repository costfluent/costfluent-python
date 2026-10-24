"""Generated from the Public API document. Do not edit."""

CONTRACT_SHA256 = "0b9a6864ae2611a073fa0ae842ea3ef2d93f3ddc716b7c59fbd2de0618cddb5f"
"""SHA-256 of the Public API document this package was generated from."""

IDEMPOTENT_CREATES: tuple[str, ...] = (
    "/v1/allocation/rules",
    "/v1/apps",
    "/v1/budgets",
    "/v1/business-metrics",
    "/v1/cost-alerts",
    "/v1/cost-report-subscriptions",
    "/v1/cost-reports",
    "/v1/custom-providers/{providerId}/costs",
    "/v1/dashboards",
    "/v1/dashboards/{dashboardId}/widgets",
    "/v1/folders",
    "/v1/providers",
    "/v1/saved-filters",
    "/v1/segments",
    "/v1/teams",
    "/v1/users",
    "/v1/virtual-tags",
    "/v1/workspace-providers",
    "/v1/workspaces",
)
"""The creates that take an Idempotency-Key; create_client sends a fresh one with each."""
