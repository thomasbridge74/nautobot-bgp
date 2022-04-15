from django.db.models import Q

from netbox.views import generic

from .filters import (
    ASNFilterSet, CommunityFilterSet, BGPSessionFilterSet,
    RoutingPolicyFilterSet, BGPPeerGroupFilterSet
)
from .models import ASN, Community, BGPSession, RoutingPolicy, BGPPeerGroup
from .tables import ASNTable, CommunityTable, BGPSessionTable, RoutingPolicyTable, BGPPeerGroupTable
from .forms import (
    ASNFilterForm, ASNBulkEditForm, ASNForm, CommunityForm,
    CommunityFilterForm, CommunityBulkEditForm, BGPSessionForm,
    BGPSessionFilterForm, BGPSessionAddForm, RoutingPolicyFilterForm,
    RoutingPolicyForm, BGPPeerGroupFilterForm, BGPPeerGroupForm
)


class ASNListView(generic.ObjectListView):
    queryset = ASN.objects.all()
    filterset = ASNFilterSet
    filterset_form = ASNFilterForm
    table = ASNTable
    action_buttons = ('add',)


class ASNView(generic.ObjectView):
    queryset = ASN.objects.all()
    template_name = 'nautobot_bgp_plugin/asn.html'

    def get_extra_context(self, request, instance):
        sess = BGPSession.objects.filter(remote_as=instance) | BGPSession.objects.filter(local_as=instance)
        sess_table = BGPSessionTable(sess)
        return {
            'related_session_table': sess_table
        }


class ASNEditView(generic.ObjectEditView):
    queryset = ASN.objects.all()
    form = ASNForm


class ASNBulkDeleteView(generic.BulkDeleteView):
    queryset = ASN.objects.all()
    table = ASNTable


class ASNBulkEditView(generic.BulkEditView):
    queryset = ASN.objects.all()
    filterset = ASNFilterSet
    table = ASNTable
    form = ASNBulkEditForm


class ASNDeleteView(generic.ObjectDeleteView):
    queryset = ASN.objects.all()


class CommunityListView(generic.ObjectListView):
    queryset = Community.objects.all()
    filterset = CommunityFilterSet
    filterset_form = CommunityFilterForm
    table = CommunityTable
    action_buttons = ('add',)


class CommunityView(generic.ObjectView):
    queryset = Community.objects.all()
    template_name = 'nautobot_bgp_plugin/community.html'


class CommunityEditView(generic.ObjectEditView):
    queryset = Community.objects.all()
    form = CommunityForm


class CommunityBulkDeleteView(generic.BulkDeleteView):
    queryset = Community.objects.all()
    table = CommunityTable


class CommunityBulkEditView(generic.BulkEditView):
    queryset = Community.objects.all()
    filterset = CommunityFilterSet
    table = CommunityTable
    form = CommunityBulkEditForm


class CommunityDeleteView(generic.ObjectDeleteView):
    queryset = Community.objects.all()


class BGPSessionListView(generic.ObjectListView):
    queryset = BGPSession.objects.all()
    filterset = BGPSessionFilterSet
    filterset_form = BGPSessionFilterForm
    table = BGPSessionTable
    action_buttons = ('add',)


class BGPSessionEditView(generic.ObjectEditView):
    queryset = BGPSession.objects.all()
    form = BGPSessionForm


class BGPSessionAddView(generic.ObjectEditView):
    queryset = BGPSession.objects.all()
    form = BGPSessionAddForm


class BGPSessionBulkDeleteView(generic.BulkDeleteView):
    queryset = BGPSession.objects.all()
    table = BGPSessionTable


class BGPSessionView(generic.ObjectView):
    queryset = BGPSession.objects.all()
    template_name = 'nautobot_bgp_plugin/bgpsession.html'

    def get_extra_context(self, request, instance):
        if instance.peer_group:
            import_policies_qs = instance.import_policies.all() | instance.peer_group.import_policies.all()
            export_policies_qs = instance.export_policies.all() | instance.peer_group.export_policies.all()
        else:
            import_policies_qs = instance.import_policies.all()
            export_policies_qs = instance.export_policies.all()

        import_policies_table = RoutingPolicyTable(
            import_policies_qs,
            orderable=False
        )
        export_policies_table = RoutingPolicyTable(
            export_policies_qs,
            orderable=False
        )

        return {
            'import_policies_table': import_policies_table,
            'export_policies_table': export_policies_table
        }


class BGPSessionDeleteView(generic.ObjectDeleteView):
    queryset = BGPSession.objects.all()


class RoutingPolicyListView(generic.ObjectListView):
    queryset = RoutingPolicy.objects.all()
    filterset = RoutingPolicyFilterSet
    filterset_form = RoutingPolicyFilterForm
    table = RoutingPolicyTable
    action_buttons = ('add',)


class RoutingPolicyEditView(generic.ObjectEditView):
    queryset = RoutingPolicy.objects.all()
    form = RoutingPolicyForm


class RoutingPolicyBulkDeleteView(generic.BulkDeleteView):
    queryset = RoutingPolicy.objects.all()
    table = RoutingPolicyTable


class RoutingPolicyView(generic.ObjectView):
    queryset = RoutingPolicy.objects.all()
    template_name = 'nautobot_bgp_plugin/routingpolicy.html'

    def get_extra_context(self, request, instance):
        sess = BGPSession.objects.filter(
            Q(import_policies=instance)
            | Q(export_policies=instance)
            | Q(peer_group__in=instance.group_import_policies.all())
            | Q(peer_group__in=instance.group_export_policies.all())
        )
        sess = sess.distinct()
        sess_table = BGPSessionTable(sess)
        return {
            'related_session_table': sess_table
        }


class RoutingPolicyDeleteView(generic.ObjectDeleteView):
    queryset = RoutingPolicy.objects.all()


class BGPPeerGroupListView(generic.ObjectListView):
    queryset = BGPPeerGroup.objects.all()
    filterset = BGPPeerGroupFilterSet
    filterset_form = BGPPeerGroupFilterForm
    table = BGPPeerGroupTable
    action_buttons = ('add',)


class BGPPeerGroupEditView(generic.ObjectEditView):
    queryset = BGPPeerGroup.objects.all()
    form = BGPPeerGroupForm


class BGPPeerGroupBulkDeleteView(generic.BulkDeleteView):
    queryset = BGPPeerGroup.objects.all()
    table = BGPPeerGroupTable


class BGPPeerGroupView(generic.ObjectView):
    queryset = BGPPeerGroup.objects.all()
    template_name = 'nautobot_bgp_plugin/bgppeergroup.html'

    def get_extra_context(self, request, instance):
        import_policies_table = RoutingPolicyTable(
            instance.import_policies.all(),
            orderable=False
        )
        export_policies_table = RoutingPolicyTable(
            instance.export_policies.all(),
            orderable=False
        )

        sess = BGPSession.objects.filter(peer_group=instance)
        sess = sess.distinct()
        sess_table = BGPSessionTable(sess)
        return {
            'import_policies_table': import_policies_table,
            'export_policies_table': export_policies_table,
            'related_session_table': sess_table
        }


class BGPPeerGroupDeleteView(generic.ObjectDeleteView):
    queryset = BGPPeerGroup.objects.all()
