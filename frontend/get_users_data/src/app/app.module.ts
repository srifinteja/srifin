import { APP_INITIALIZER, NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import {HttpClientModule} from '@angular/common/http';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { FormsModule } from '@angular/forms';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MatSidenavModule } from '@angular/material/sidenav';
import { MatListModule } from '@angular/material/list';
import { MatMenuModule } from '@angular/material/menu';
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatIconModule } from '@angular/material/icon';
import { SafeUrlPipe } from './safe-url.pipe';
import { MapComponent } from './map/map.component';
import { LegendComponent } from './legend/legend.component';
import { Legend2Component } from './legend2/legend2.component';
import { Legend3Component } from './legend3/legend3.component';
// Import Angular Material Modules
import { MatExpansionModule } from '@angular/material/expansion';
import { MatTableModule } from '@angular/material/table';
import { CommonModule } from '@angular/common';
import { KeycloakAngularModule, KeycloakService } from 'keycloak-angular';
import { initializeKeycloak } from 'keycloak-init.factory';
// function initkey(keycloak:KeycloakService){
//   return()=>
//     keycloak.init({
//       config:{
//         url:'http://localhost:8180',
//         realm:'srifin',
//         clientId:'srifin_client',
//       },
//       initOptions: {
//         onLoad: 'check-sso',
//         silentCheckSsoRedirectUri:
//           window.location.origin + '/assets/silent-check-sso.html',
//         checkLoginIframe: false,
//         redirectUri: 'http://localhost:4200',
//       },
//     });
// }
@NgModule({
  declarations: [
    AppComponent,
    SafeUrlPipe,
    MapComponent,
    LegendComponent,
    Legend2Component,
    Legend3Component
  ],
  imports: [
    BrowserModule,
    FormsModule,
    AppRoutingModule,
    HttpClientModule,
    BrowserAnimationsModule,
    MatSidenavModule,
    MatListModule,
    MatMenuModule,
    MatToolbarModule,
    MatIconModule,
    MatExpansionModule,
    MatTableModule,
    CommonModule,
    KeycloakAngularModule
  ],
  providers: [
    {
      provide: APP_INITIALIZER,
      useFactory: initializeKeycloak,
      multi: true,
      deps: [KeycloakService],
    },
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
