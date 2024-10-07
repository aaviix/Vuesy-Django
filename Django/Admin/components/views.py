from django.shortcuts import render
from django.views.generic import TemplateView 
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class ComponentsView(LoginRequiredMixin,TemplateView):
    pass

# forms
forms_elements_view = ComponentsView.as_view(template_name = "components/forms/form-elements.html")
forms_validation_view = ComponentsView.as_view(template_name = "components/forms/form-validation.html")
forms_advanced_view = ComponentsView.as_view(template_name = "components/forms/form-advanced.html")
forms_editors_view = ComponentsView.as_view(template_name = "components/forms/form-editors.html")
forms_file_uploads_view = ComponentsView.as_view(template_name = "components/forms/form-uploads.html")
forms_wizard_view = ComponentsView.as_view(template_name = "components/forms/form-wizard.html")
forms_mask_view = ComponentsView.as_view(template_name = "components/forms/form-mask.html")

# tables
tables_basic_view = ComponentsView.as_view(template_name = "components/tables/tables-basic.html")
tables_advanced_view = ComponentsView.as_view(template_name = "components/tables/tables-advanced.html")

# apex charts
apexcharts_line_view = ComponentsView.as_view(template_name = "components/apex-charts/charts-line.html")
apexcharts_area_view = ComponentsView.as_view(template_name = "components/apex-charts/charts-area.html")
apexcharts_column_view = ComponentsView.as_view(template_name = "components/apex-charts/charts-column.html")
apexcharts_bar_view = ComponentsView.as_view(template_name = "components/apex-charts/charts-bar.html")
apexcharts_mixed_view = ComponentsView.as_view(template_name = "components/apex-charts/charts-mixed.html")
apexcharts_timeline_view = ComponentsView.as_view(template_name = "components/apex-charts/charts-timeline.html")
apexcharts_candlestick_view = ComponentsView.as_view(template_name = "components/apex-charts/charts-candlestick.html")
apexcharts_boxplot_view = ComponentsView.as_view(template_name = "components/apex-charts/charts-boxplot.html")
apexcharts_bubble_view = ComponentsView.as_view(template_name = "components/apex-charts/charts-bubble.html")
apexcharts_scatter_view = ComponentsView.as_view(template_name = "components/apex-charts/charts-scatter.html")
apexcharts_heatmap_view = ComponentsView.as_view(template_name = "components/apex-charts/charts-heatmap.html")
apexcharts_treemap_view = ComponentsView.as_view(template_name = "components/apex-charts/charts-treemap.html")
apexcharts_pie_view = ComponentsView.as_view(template_name = "components/apex-charts/charts-pie.html")
apexcharts_radialbar_view = ComponentsView.as_view(template_name = "components/apex-charts/charts-radialbar.html")
apexcharts_radar_view = ComponentsView.as_view(template_name = "components/apex-charts/charts-radar.html")
apexcharts_polararea_view = ComponentsView.as_view(template_name = "components/apex-charts/charts-polararea.html")

# icons
icons_unicons_view = ComponentsView.as_view(template_name = "components/icons/icons-unicons.html")
icons_feathericons_view = ComponentsView.as_view(template_name = "components/icons/icons-feathericons.html")
icons_boxicons_view = ComponentsView.as_view(template_name = "components/icons/icons-boxicons.html")
icons_materialdesign_view = ComponentsView.as_view(template_name = "components/icons/icons-materialdesign.html")
icons_fontawesome_view = ComponentsView.as_view(template_name = "components/icons/icons-fontawesome.html")

# maps
maps_google_view = ComponentsView.as_view(template_name = "components/maps/maps-google.html")
maps_vector_view = ComponentsView.as_view(template_name = "components/maps/maps-vector.html")
maps_leaflet_view = ComponentsView.as_view(template_name = "components/maps/maps-leaflet.html")


