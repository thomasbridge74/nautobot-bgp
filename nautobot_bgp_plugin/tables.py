import django_tables2 as tables
from django.utils.safestring import mark_safe
from django_tables2.utils import A

from netbox.tables import NetBoxTable
from netbox.tables.columns import ChoiceFieldColumn, TagColumn

from .models import ASN, Community, BGPSession, RoutingPolicy, BGPPeerGroup

AVAILABLE_LABEL = mark_safe('<span class="label label-success">Available</span>')
COL_TENANT = """
 {% if record.tenant %}
     <a href="{{ record.tenant.get_absolute_url }}" title="{{ record.tenant.description }}">{{ record.tenant }}</a>
 {% else %}
     &mdash;
 {% endif %}
 """

POLICIES = """
{% for rp in value.all %}
    <a href="{{ rp.get_absolute_url }}">{{ rp }}</a>{% if not forloop.last %}<br />{% endif %}
{% empty %}
    &mdash;
{% endfor %}
"""


class ASNTable(NetBoxTable):
    number = tables.LinkColumn(text=lambda record: record.__str__(), args=[A("pk")])
    status = ChoiceFieldColumn(default=AVAILABLE_LABEL)
    site = tables.LinkColumn()
    tenant = tables.TemplateColumn(template_code=COL_TENANT)

    class Meta(NetBoxTable.Meta):
        model = ASN
        fields = ("pk", "number", "description", "status", "tenant")


class CommunityTable(NetBoxTable):
    value = tables.LinkColumn()
    status = ChoiceFieldColumn(default=AVAILABLE_LABEL)
    tenant = tables.TemplateColumn(template_code=COL_TENANT)
    tags = TagColumn(url_name="plugins:nautobot_bgp_plugin:community_list")

    class Meta(NetBoxTable.Meta):
        model = Community
        fields = ("pk", "value", "description", "status", "tenant", "tags")
        default_columns = ("pk", "value", "description", "status", "tenant")


class BGPSessionTable(NetBoxTable):
    name = tables.LinkColumn()
    device = tables.LinkColumn()
    local_address = tables.LinkColumn()
    local_as = tables.LinkColumn()
    remote_address = tables.LinkColumn()
    remote_as = tables.LinkColumn()
    site = tables.LinkColumn()
    peer_group = tables.LinkColumn()
    status = ChoiceFieldColumn(default=AVAILABLE_LABEL)
    tenant = tables.TemplateColumn(template_code=COL_TENANT)

    class Meta(NetBoxTable.Meta):
        model = BGPSession
        fields = (
            "pk",
            "name",
            "device",
            "local_address",
            "local_as",
            "remote_address",
            "remote_as",
            "description",
            "peer_group",
            "site",
            "status",
            "tenant",
        )
        default_columns = (
            "pk",
            "name",
            "device",
            "local_address",
            "local_as",
            "remote_address",
            "remote_as",
            "description",
            "site",
            "status",
            "tenant",
        )


class RoutingPolicyTable(NetBoxTable):
    name = tables.LinkColumn()

    class Meta(NetBoxTable.Meta):
        model = RoutingPolicy
        fields = ("pk", "name", "description")


class BGPPeerGroupTable(NetBoxTable):
    name = tables.LinkColumn()
    import_policies = tables.TemplateColumn(template_code=POLICIES, orderable=False)
    export_policies = tables.TemplateColumn(template_code=POLICIES, orderable=False)
    tags = TagColumn(url_name="plugins:nautobot_bgp_plugin:peer_group_list")

    class Meta(NetBoxTable.Meta):
        model = BGPPeerGroup
        fields = (
            "pk",
            "name",
            "description",
            "tags",
            "import_policies",
            "export_policies",
        )
        default_columns = ("pk", "name", "description")
