import { NgModule } from "@angular/core";
import { Routes, RouterModule } from "@angular/router";
import { LineChartComponent } from "./line-chart/line-chart.component";
import { HttpClientModule } from "@angular/common/http";

const routes: Routes = [
  { path: "", pathMatch: "full", redirectTo: "line-chart" },
  { path: "line-chart", component: LineChartComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes), HttpClientModule],
  exports: [RouterModule]
})
export class AppRoutingModule {
}
