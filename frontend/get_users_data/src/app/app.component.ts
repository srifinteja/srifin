import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { NgForm } from '@angular/forms';
import { DomSanitizer, SafeResourceUrl } from '@angular/platform-browser';
import { ChangeDetectorRef } from '@angular/core';
import {  EventEmitter, Output } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MatExpansionModule } from '@angular/material/expansion';
import { MatListModule } from '@angular/material/list'; // If not already imported
import { map } from 'leaflet';
import { User, negativeMaps } from './map/census-data';
import 'chartjs-adapter-date-fns';
import { Icon  } from 'ol/style';
import { FeatureLike } from 'ol/Feature';
import {  ChartConfiguration, registerables } from 'chart.js';
import { StyleFunction } from 'ol/style/Style';
import { Observable, sequenceEqual } from 'rxjs';
import {Circle as CircleStyle, Fill, Stroke, Style } from 'ol/style';
import Map from 'ol/Map';
import VectorSource from 'ol/source/Vector';
import VectorLayer from 'ol/layer/Vector';
import { LineString, Point,Geometry } from 'ol/geom';
import TileLayer from 'ol/layer/Tile';
import OSM from 'ol/source/OSM';
import View from 'ol/View';
import { Coordinate } from 'ol/coordinate';
Chart.register(...registerables);
import Chart from 'chart.js/auto';
import { KeycloakService } from 'keycloak-angular';
import { Feature } from 'ol';
import { fromLonLat, useGeographic } from 'ol/proj';
import { Attribution, defaults as defaultControls } from 'ol/control';
import { CommonModule,DatePipe } from '@angular/common';
type LocationId = "kala" | "basa" | "yadg" | "bija" | "kama" | "have" | "bela" | "chit" | "loka" | "goka" |
  "sham" | "hubb" | "shah" | "rane" | "darb" | "sakr" | "phul" | "runn" | "beni" | "sahe" | 
  "rose" | "sheo" | "kant" | "sita" | "sama" | "hath" | "jale" | 
  "shiv" | "gora" | "chau" | "tund" | "alig" | "ikau" | "khad" | "capt" | 
  "tara" | "maho" | "nich" | "kira" | "mix" | "latestSourcing" | "kitt"|
  "combined" | "under15" | "census";



  interface DeviceIdCount {
    deviceId: string;
    count: number;
    speed:string;
    time: string;
    distance:string;
    avg_speed:string;
    start_date:string;
    end_date:string;
    timeDifference :string;
  
  }
  
  // Define a dataset interface to type the datasets
  interface DataSet {
    label: string;
    data: number[];
    borderColor: string;
    pointBackgroundColor: string;
    fill: boolean;
    borderWidth: number;
    pointRadius: number;
  }
  


interface Location {
  id: LocationId;
  name: string;
  
}
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  title = 'frontend';
  optionsDropdownVisibility: { [key: string]: boolean } = {};
  externalUrl: SafeResourceUrl | null = null;
  showMap: boolean = false;
  showUnder15 : boolean = false;
  showSource : boolean = false;
  showMix:boolean=false;
  dropdownOpen = false;
  chart: any;
  activeDataset: string = '';
  sidenavOpen: boolean = false;
  showDashboardDropdown = false;
  showwest = false;
  showeast = false;
  showKaDropdown = false;
  showBrDropdown = false;
  mapp:boolean = false;
  // routeLayer: VectorLayer;
  isLoggedIn: boolean = false;
  routeLayerVisible: boolean = true; // Initial visibility of the route layer
  showUpDropdown = false;
  // branches = ['shivpur']; // Example branch names
  // selectedBranch: string;
  map!: Map;
  maps: string| null = null;
  isKalaburgiUser: boolean = false;
  // scriptOutput: string = '';
  isLoading: boolean = false;
  isBasavUser: boolean=false;
  mapM:string|null = null;
  activeMap: string | null = null;
  showTable = false;
  show_error:boolean = true;
  negativeData_up: negativeMaps[] = [];
  negativeData: negativeMaps[] = [];
  negativeData_ka: negativeMaps[] = [];
  negativeData_br: negativeMaps[] = [];
  scriptOutput?: string;
  // mapType: string;
  displayedColumns: string[] = ['branch', 'latestApplication', 'pincode', 'jun23Cat', 'recordedPincode', 'recordedPincodeCat', 'censuscode2011', 'village', 'district', 'state', 'ur', 'initiatedCen', 'cgt1Cen', 'cgt2Cen', 'grtCen', 'activeCen', 'loanApps', 'cbFail', 'cbDone', 'cgt1', 'cgt2', 'grt', 'disbursed'];
  dataSource: negativeMaps[] = [];
  shownegativetable_br: boolean = false;
  shownegativetable_ka: boolean = false;
  shownegativetable_up: boolean = false;
  private routeLayer: VectorLayer<VectorSource<Feature<Geometry>>> | null = null;
  currentDataset = ''; // default dataset
  mapType: "census" | "under15" | "combined" | "latestSourcing" | 
  "kala" | "basa" | "yadg" | "bija" | "kama" | "have" | "bela" | "chit" | "loka" | "goka" |
  "sham" | "hubb" | "shah" | "rane" | "darb" | "sakr" | "phul" | "runn" | "beni" | "sahe" | 
  "rose" | "sheo" | "kant" | "sita" | "sama" | "hath" | "jale" | "kitt"|
  "shiv" | "gora" | "chau" | "tund" | "alig" | "ikau" | "khad" | "capt" | 
  "tara" | "maho" | "nich" | "kira" | "mix" ;
  mapt: string = '';
  mapS:string = '';
  sample:string = 'teja';
  isVisible: boolean = false;
  kalocations: Location[] =[
    { id: 'kala', name: 'Kalaburgi' },
    { id: 'basa', name: 'Basavakalyan' },
    { id: 'yadg', name: 'Yadgir' },
    { id: 'bija', name: 'Bijapur' },
    { id: 'kama', name: 'Kamalapur' },
    { id: 'have', name: 'Haveri' },
    { id: 'bela', name: 'Belagavi' },
    { id: 'chit', name: 'Chitguppa' },
    { id: 'loka', name: 'Lokapur' },
    { id: 'goka', name: 'Gokak' },
    { id: 'sham', name: 'Shamanur' },
    { id: 'hubb', name: 'Hubbali' },
    { id: 'shah', name: 'Shahpur' },
    { id: 'rane', name: 'Ranebennur' },
    { id: 'kitt', name: 'Kittur'}
   
    
  ];
  brlocations: Location[] =[
  { id: 'darb', name: 'Darbhanga' },
    { id: 'sakr', name: 'Sakri' },
    { id: 'phul', name: 'Phulparas' },
    { id: 'runn', name: 'Runnisaidpur' },
    { id: 'beni', name: 'Benipur' },
    { id: 'sahe', name: 'Sahebganj' },
    { id: 'rose', name: 'Rosera' },
    { id: 'sheo', name: 'Sheohar' },
    { id: 'kant', name: 'Kanti' },
    { id: 'sita', name: 'Sitamarhi' },
    { id: 'sama', name: 'Samastipur' },
  
  ];
  uplocations_west:Location[]=[
    { id: 'hath', name: 'Hathras' },
    { id: 'jale', name: 'Jalesar' },
    { id: 'tund', name: 'Tundla' },
    { id: 'alig', name: 'Aligarh' },
    { id: 'kira', name: 'Kiraoli' },
  ];
    uplocations_east:Location[]=[
    { id: 'shiv', name: 'Shivpur' },
    { id: 'gora', name: 'Gorakhpur' },
    { id: 'chau', name: 'Chauri Chaura' },
    { id: 'ikau', name: 'Ikauna' },
    { id: 'khad', name: 'Khadda' },
    { id: 'capt', name: 'Captainganj' },
    { id: 'tara', name: 'Tarabganj' },
    { id: 'maho', name: 'Mahoba' },
    { id: 'nich', name: 'Nichlaul' },
    

  ];
  showOptionsDropdown = false; // To control the visibility of options dropdown
  currentMapType: string | null = null;
 
  // Common options for all maps
  // options = ['15km radius', 'sourcing status', 'overall activity'];
  options = ['overall activity'];
  // maps = [
  //   { id: 'kalb', name: 'Kalaburgi' },
  //   { id: 'basa', name: 'Basavakalyan' },
  //   // Add other maps here
  // ];
toggleTable(){
  this.showTable = !this.showTable;
  this.showUnder15 = false;
  this.showMap = false;
  // this.showTable = false;
  this.showSource = false;
  this.showMix = false;
  this.showeast = false;
      this.showwest = false;
  this.isVisible = false;
   
}
parseJsonString(value: string): any[] {
  try {
    return JSON.parse(value);
  } catch (e) {
    return []; // return an empty array if parsing fails
  }
}

  setActiveMap(mapId: string): void {
    this.activeMap = mapId;
  }
  toggleDashboardDropdown() {
    // Close the map if the dropdown is being closed
   
      this.showMap = false;
      this.externalUrl = false;
      this.showTable =false;
    this.showDashboardDropdown = !this.showDashboardDropdown;
    this.showeast = false;
      this.showwest = false;
    this.isVisible = false;
  }
  toggkalb :boolean = false;
  togginkalb :boolean = false;
  togghub:boolean=false;
  togsham:boolean=false;
  toggok:boolean = false;
  toggdarb:boolean = false;
  toggindarb:boolean = false;
  togmuza:boolean = false;
  toggmath:boolean = false;
  togmeer:boolean = false;
  togmath:boolean = false;
  togayo:boolean = false;
  toggor:boolean =false;
  togkus:boolean = false;
  togchi:boolean = false;
  togglekalb(){
    this.toggkalb  = !this.toggkalb;
  }
  toggleinkalb(){
    this.togginkalb = !this.togginkalb;
  }
  togglehub(){
this.togghub = !this.togghub;
  }
  toggsham(){
this.togsham = !this.togsham;
  }
  togggoka(){
this.toggok = !this.toggok;
  }
  toggledarb(){
this.toggdarb = !this.toggdarb;
  }
  toggleindarb(){
this.toggindarb = !this.toggindarb;
  }
  toggmuza(){
this.togmuza = !this.togmuza;
  }
  toggleMath(){
    this.toggmath = !this.toggmath;
  }
  toggleMeer(){
    this.togmeer = !this.togmeer;
  }
  toggleinMath(){
    this.togmath = !this.togmath;
  }
  toggAyodh(){
    this.togayo = !this.togayo;
  }
  toggGora(){
    this.toggor  = !this.toggor;
  }
  toggKush(){
    this.togkus = !this.togkus;
  }
  toggChit(){
    this.togchi = !this.togchi;
  }
  toggleKaDropdown() {
    // Close the map if the dropdown is being closed
   
      this.showMap = false;
      this.externalUrl = false;
      this.showDashboardDropdown = false;
      this.showUpDropdown = false;
      this.showBrDropdown = false;
      this.showTable =false;
    this.showKaDropdown = !this.showKaDropdown;
    this.showeast = false;
      this.showwest = false;
    this.isVisible = false;
  }

  toggleBrDropdown() {
    // Close the map if the dropdown is being closed
   
      this.showMap = false;
      this.externalUrl = false;
      this.showDashboardDropdown = false;
      this.showKaDropdown = false;
      this.showUpDropdown = false;
      this.showTable =false;
      this.showUnder15  = false;
      this.showSource = false;
    this.showBrDropdown = !this.showBrDropdown;
    this.showeast = false;
      this.showwest = false;
    this.isVisible = false;
  }

  toggleUpDropdown() {
    // Close the map if the dropdown is being closed
   
      this.showMap = false;
      this.externalUrl = false;
      this.showDashboardDropdown = false;
      this.showKaDropdown = false;
      this.showTable =false;
      this.showBrDropdown = false;
      this.isVisible = false;
      // this.showeast = false;
      // this.showwest = false;
    this.showUpDropdown = !this.showUpDropdown;
  }


  toggleUpWestDropdown() {
    // Close the map if the dropdown is being closed
   
     this.showwest = !this.showwest; 
    //  this.showeast = false;
  }

  toggleUpeastDropdown() {
    // Close the map if the dropdown is being closed
    
    this.showeast = !this.showeast;
    this.cdr.detectChanges();  // Force change detection
    
  //  this.showeast = !this.showeast;
  //  this.showwest = false;
  
  }

  onBranchChange($event: Event) {
    const value = ($event.target as HTMLSelectElement)?.value;
    if (value) {
      // this.selectedBranch = value;
    }
  }
  
  userName: string = '';
  constructor(
    private http: HttpClient,
    private sanitizer: DomSanitizer,
    private cdr: ChangeDetectorRef,
    private keycloakService: KeycloakService
    
  ) {
    
    // this.selectedBranch = this.branches[0];
    this.mapType = "census";
    
  }
  // "C:\\Users\\Teja\\AppData\\Local\\Programs\\Python\\Python312\\python3.dll", "C:\\Users\\Teja\\Desktop\\All_codes\\Combined_code_village.py"
  ngOnInit() {
    this.isLoggedIn = this.keycloakService.isLoggedIn();
    this.loadUserProfile();
    this.checkUserRole();
    this.map = new Map({
      target: 'map',
      layers: [
        new TileLayer({
          source: new OSM()
        })
      ],
      view: new View({
        center: [0, 0],
        zoom: 2
      }),
       // Use 'new' to instantiate controls
       controls: defaultControls().extend([
        new Attribution({
            collapsible: false
        })
      ])
    });
    this.x();

    this.kalocations.forEach(location => {
      this.optionsDropdownVisibility[location.id] = false;
    });
  
    this.fetchData(this.currentDataset);

  }
  async loadUserProfile() {
    try {
      const userDetails = await this.keycloakService.loadUserProfile();
      console.log(userDetails.username);
      this.userName = userDetails.username|| 'Guest';
    } catch (error) {
      console.error('Error loading user details', error);
    }
  }

  logout() {
    this.keycloakService.logout();
  }
  login() {
    this.keycloakService.login();
  }
  
  private renderChart(users: User[]): void {
    const canvas = document.getElementById('canvas') as HTMLCanvasElement;
    if (!canvas) {
      console.error("Canvas element not found.");
      return;
  }
    const ctx = canvas.getContext('2d');
    if (!ctx) {
      console.error("2D context not supported.");
      return;
    }

    const timeLabels = users.map(user => user.humanReadableDate);
    
    const datasets = this.categorizeData(users);
    
    
    this.chart?.destroy();

    this.chart = new Chart(ctx, {
      type: 'line',
      data: {
        labels: timeLabels,
        datasets: datasets
      },
      options: this.getChartOptions()
    });

    // this.setupZoomButtons();
  }
  private async checkUserRole() {
    const userDetails = await this.keycloakService.loadUserProfile();
    // Assuming there's a custom attribute or a role that can be checked
    this.isKalaburgiUser = userDetails.username==='user';
    this.isBasavUser = userDetails.username==='user1';
  }
  private categorizeData(users: User[]): DataSet[] {
    const stationaryData: DataSet = { label: 'Stationary (Speed < 3 km/hr)', data: [], borderColor: 'red', pointBackgroundColor: 'red', fill: false, borderWidth: 1, pointRadius: 2 };
    const walkingData: DataSet = { label: 'Walking (3 km/hr ≤ Speed ≤ 10 km/hr)', data: [], borderColor: 'green', pointBackgroundColor: 'green', fill: false, borderWidth: 1, pointRadius: 2 };
    const bikingData: DataSet = { label: 'Biking (Speed > 10 km/hr)', data: [], borderColor: 'blue', pointBackgroundColor: 'blue', fill: false, borderWidth: 1, pointRadius: 2 };

    users.forEach(user => {
        if (user.mov_avg_spd < 3) {
            stationaryData.data.push(user.mov_avg_spd);
        } else if (user.mov_avg_spd <=10) {
            walkingData.data.push(user.mov_avg_spd);
        } else {
            bikingData.data.push(user.mov_avg_spd);
        }
    });

    return [stationaryData, walkingData, bikingData];
}

private clearExistingRoute() {
  if (this.routeLayer) {
    this.map.removeLayer(this.routeLayer);
    this.routeLayer = null;
  }
}
getRouteLayer(): VectorLayer<VectorSource<Feature<Geometry>>>|null {
  return this.routeLayer;
}

togglemapp():void{
  this.mapp = !this.mapp;
}
toggleRouteLayer(): void {
  
  this.routeLayerVisible = !this.routeLayerVisible;
  if (this.routeLayer) {
    this.routeLayer.setVisible(this.routeLayerVisible);
  }
}
// Add a new route layer
private addRouteLayer(vectorSource: VectorSource<Feature<Geometry>>): void {
  this.routeLayer = new VectorLayer({
    source: vectorSource,
  });
  this.map.addLayer(this.routeLayer);
}
formattedEndDate = new Date();

  // Create a new Date object for the start date, then subtract 24 hours
  formattedStartDate = new Date(this.formattedEndDate.getTime() - 3*24 * 60 * 60 * 1000);

transformDate(date: Date): string {
  let year = date.getFullYear();
  let month = (date.getMonth() + 1).toString().padStart(2, '0'); // Months are zero-indexed
  let day = date.getDate().toString().padStart(2, '0');
  let hours = date.getHours().toString().padStart(2, '0');
  let minutes = date.getMinutes().toString().padStart(2, '0');
  console.log(`${year}-${month}-${day}T${hours}:${minutes}`);
  return `${year}-${month}-${day}T${hours}:${minutes}`;
}
 startDate = this.transformDate(this.formattedStartDate);
 endDate = this.transformDate(this.formattedEndDate);


deviceId:string = '9315638429';
// startDate:string = '2024-04-21 14:30:50';
// endDate:string='2024-04-25 14:30:50';
originalUsers: User[] = []; 
x():void{
  
  let url:string = `http://localhost:8080/api/census?`;
  if (this.deviceId) {
    url += `deviceId=${this.deviceId}`;
  }
  if (this.startDate) {
    url += `&startTime=${encodeURIComponent(this.startDate)}`;
  }
  if (this.endDate) {
    url += `&endTime=${encodeURIComponent(this.endDate)}`;
  }
  
this.loadPath(url);
//   this.http.get<any>(url).subscribe(
//     response => {
  
//       if (response && response.content && typeof response.totalPages === 'number') {
//         // this.totalDistance = 0;

//      // Apply type to the filter function's parameter
//      const filteredUsers = response.content;

//         this.originalUsers = filteredUsers.map((user: any) => {
//           // this.totalDistance += parseFloat(user.delta_distance) || 0;
//           return {
//             ...user,
//             isActive: true
//           };
//         });

//         // this.users = [...this.originalUsers];
//         this.renderChart(this.originalUsers);
//       }
//     }
//   );
  }
  // loadPath(url: string) {
  //   this.clearExistingRoute();
  //   this.http.get<{ content: any[] }>(url).subscribe({
  //     next: (response) => {
  //       if (response.content && Array.isArray(response.content)) {
  //         const coordinates = response.content.map(point => fromLonLat([point.longitude, point.latitude]) as Coordinate);
  
  //         const pathFeature = new Feature(new LineString(coordinates));
  // // Create start and end point features
  // const startPointFeature = new Feature(new Point(coordinates[0]));
  // const endPointFeature = new Feature(new Point(coordinates[coordinates.length - 1]));
  
  //         // Styles for start and end points
  //         const startStyle = new Style({
  //           image: new CircleStyle({
  //             radius: 7,
  //             fill: new Fill({ color: 'green' }),
  //             stroke: new Stroke({ color: 'black', width: 2 })
  //           })
  //         });
  
  //         const endStyle = new Style({
  //           image: new CircleStyle({
  //             radius: 7,
  //             fill: new Fill({ color: 'red' }),
  //             stroke: new Stroke({ color: 'black', width: 2 })
  //           })
  //         });
  
  //         startPointFeature.setStyle(startStyle);
  //         endPointFeature.setStyle(endStyle);
  
  //         // Add to vector source
  //         const vectorSource = new VectorSource({
  //           features: [pathFeature, startPointFeature, endPointFeature]
  //         });
         
  
  //         this.routeLayer = new VectorLayer({
  //           source: vectorSource,
  //           style: this.createPathStyle()
  //         });
  
  //         this.map.addLayer(this.routeLayer);
  //         // Adjust map view
  //         if (coordinates.length > 0) {
  //           this.map.getView().fit(vectorSource.getExtent(), {
  //             padding: [50, 50, 50, 50], // Adjust padding as needed
  //             maxZoom: 17, // Prevents the map from zooming in too far
  //           });
  //         }
  //       } else {
  //         console.error('Data is not in expected format:', response);
  //       }
  //     },
  //     error: (err) => {
  //       console.error('Error loading path data:', err);
  //     }
  //   });
  // }
  loadPath(url: string) {
    this.clearExistingRoute(); // Ensure this method clears the previous route from the map
    this.http.get<{ content: any[] }>(url).subscribe({
      next: response => {
        if (response.content && Array.isArray(response.content)) {
          this.createAndDisplayRoute(response.content);
        } else {
          console.error('Data is not in expected format:', response);
        }
      },
      error: err => {
        console.error('Error loading path data:', err);
      }
    });
  }
  private createPointStyle(color: string): Style {
    return new Style({
      image: new CircleStyle({
        radius: 7,  // Size of the point
        fill: new Fill({ color: color }),  // Fill color of the point
        stroke: new Stroke({
          color: 'black',  // Border color of the point
          width: 2  // Border thickness
        })
      })
    });
  }
  
  private createAndDisplayRoute(data: any[]) {
    
    const coordinates = data.map(point => fromLonLat([point.longitude, point.latitude]) as Coordinate);
    const temp = data;
    const pathFeature = new Feature(new LineString(coordinates));
    const startPointFeature = new Feature(new Point(coordinates[0]));
    const endPointFeature = new Feature(new Point(coordinates[coordinates.length - 1]));
    startPointFeature.setStyle(this.createPointStyle('green'));
    endPointFeature.setStyle(this.createPointStyle('red'));

    const vectorSource = new VectorSource({
      features: [pathFeature, startPointFeature, endPointFeature]
    });

    this.routeLayer = new VectorLayer({
      source: vectorSource,
      style: this.createPathStyle() // Define this method to style the route line
    });

    this.map.addLayer(this.routeLayer);
    this.map.getView().fit(vectorSource.getExtent(), {
      padding: [50, 50, 50, 50],
      maxZoom: 17
    });
  }
  
private createPathStyle(): StyleFunction {
  return (feature: FeatureLike, resolution: number): Style[] => {
    // Get the geometry as a LineString; be careful with direct casting
    const geometry = feature.getGeometry();
    if (!(geometry instanceof LineString)) return []; // Ensure it's a LineString

    const styles: Style[] = [
      new Style({
        stroke: new Stroke({
          color: '#0000FF',
          width: 2
        })
      })
    ];

    // Adding direction arrows; only if geometry is LineString and not RenderFeature
    if (geometry instanceof LineString) {
      geometry.forEachSegment((start, end) => {
        const dx = end[0] - start[0];
        const dy = end[1] - start[1];
        const rotation = Math.atan2(dy, dx);
        styles.push(new Style({
          geometry: new Point(end),
          image: new Icon({
            src: 'assets/arrow.png',
            anchor: [0.5, 0.5],
            rotateWithView: true,
            rotation: -rotation,
            scale: 0.5
          }),
        // zIndex : 10
        }));
      });
    }

    return styles;
  };
}
private isArrowIcon(style: Style): boolean {
  const image = style.getImage();
  return image instanceof Icon && image.getSrc() === 'assets/arrow.png';
}


private getChartOptions() {
  return {
    responsive: true,
    plugins: {
      legend: {
        display: true,
        position: 'top' as const,
      },
      zoom: {
        pan: {
          enabled: true,
          mode: 'x' as const,
        },
        zoom: {
          wheel: { enabled: true },
          pinch: { enabled: true },
          mode: 'x' as const,
        },
      },
    },
    scales: {
      x: {
        type: 'time' as const,
        time: { unit: 'minute' as const },
        title: { display: true, text: 'Time', color: '#333' },
        ticks: { color: '#666' },
      },
      y: {
        title: { display: true, text: 'Moving avg Speed (km/hr)', color: '#333' },
        ticks: { color: '#666' },
      }
    }
  };
}

  runPythonScripts() {
    return this.http.post('http://localhost:8080/api/census/api/runPythonScripts', {},{responseType: 'text'});
  }
  fetchData(dataset: string) {
    this.activeDataset = dataset;
    this.getNegativeData(dataset).subscribe(
      data => {
        this.isVisible = !this.isVisible;
        this.negativeData = data;
      },
      error => {
        console.error('Error fetching data:', error);
      }
    );
  }
  getNegativeData(dataset: string): Observable<negativeMaps[]> {
    return this.http.get<negativeMaps[]>(`http://localhost:8080/api/census/${dataset}_negativeData`);
  }

  changeDataset(dataset: string) {
    this.currentDataset = dataset;
    this.fetchData(dataset);
  }
  goToProfile() {
    // Implement navigation logic here
  }

  // Log out the user
  logOut() {
    // Implement log out logic here
  }
  

  redirectToSrifin(): void {
    this.externalUrl = this.sanitizer.bypassSecurityTrustResourceUrl('https://srifincreditproduct.srifin.com/');
    this.showMap = false; 
  }

getNegative_up(): Observable<negativeMaps[]> {
  return this.http.get<negativeMaps[]>('http://localhost:8080/api/census/up_negativeData');
}
getNegative_ka(): Observable<negativeMaps[]> {
  return this.http.get<negativeMaps[]>('http://localhost:8080/api/census/ka_negativeData');
}
getNegative_br(): Observable<negativeMaps[]> {
  const x =  this.http.get<negativeMaps[]>('http://localhost:8080/api/census/br_negativeData');
  
  return x;
}


  toggleDropdown(): void {
    this.dropdownOpen = !this.dropdownOpen;
    this.isVisible = false;
   
  }
  

  // }
  toggleSidenav(): void {
    
    this.sidenavOpen = !this.sidenavOpen;
  }

  Map(): void {

    this.externalUrl = this.sanitizer.bypassSecurityTrustResourceUrl('https://www.google.com/maps/d/embed?mid=1-lRiLO7SQSdt73Udz9k_sKrlEuOVu1o&ehbc=2E312F');
    this.showMap = false;
  }
 


 
  // selectMap(mapType: "census" | "under15" | "combined") {
  //   // Hide the map with a small delay
  //   this.showMap = false;
  //   this.externalUrl = null;
  //   setTimeout(() => {
  //     // Update the map type
  //     this.mapType = mapType;
  //     // Show the map after updating the map type, only if it was previously shown
  //     if (this.showDashboardDropdown) {
  //       this.showMap = true;
  //     }
  //   }, 100); // 100 milliseconds delay
  // }
  clicked(mapType: "census" | "under15" | "combined" | "latestSourcing" | 
  "kala" | "basa" | "yadg" | "bija" | "kama" | "have" | "bela" | "chit" | "loka" | "goka" |
  "sham" | "hubb" | "shah" | "rane" | "darb" | "sakr" | "phul" | "runn" | "beni" | "sahe" | 
  "rose" | "sheo" | "kant" | "sita" | "sama"| "hath" | "jale" | "kitt"|
  "shiv" | "gora" | "chau" | "tund" | "alig" | "ikau" | "khad"  | "capt" | 
   "tara" | "maho" | "nich" | "kira" | "mix"){
    this.currentMapType = mapType;
    this.showOptionsDropdown = true;
    this.showeast = false;
      this.showwest = false;
      this.isVisible = false;
    this.toggleOptionsDropdown(mapType);
  }
  toggleOptionsDropdown(locationId: string): void {
    this.optionsDropdownVisibility[locationId] = !this.optionsDropdownVisibility[locationId];
    
    // Optional: Close other dropdowns when one is opened
    Object.keys(this.optionsDropdownVisibility).forEach(id => {
      if (id !== locationId) {
        this.optionsDropdownVisibility[id] = false;
      }
    });
  }
  selecttMap(mapt:string){
    // this.currentMapType = mapt;
    this.showOptionsDropdown = true;
    
  this.showUnder15 = false;
  this.showMap = false;
  this.showTable = false;
  this.showSource = false;
  this.externalUrl = null;
  this.showeast = false;
      this.showwest = false;
  this.showMix = false;
  this.isVisible = false;
  setTimeout(() => {
    // Update the map type
    this.mapt = mapt;
    // Show the map after updating the map type
    this.showUnder15 = true;
  }, 100); // 100 milliseconds delay
  }
  selecttSource(mapS:string){
    // this.currentMapType = mapt;
    this.showOptionsDropdown = true;
    
  this.showSource = false;
  this.showMap = false;
  this.showTable = false;
  this.showUnder15 = false;
  this.externalUrl = null;
  this.showeast = false;
      this.showwest = false;
  this.showMix = false;
  this.isVisible = false;
  setTimeout(() => {
    // Update the map type
    this.mapS = mapS;
    // Show the map after updating the map type
    this.showSource = true;
  }, 100); // 100 milliseconds delay
  }

  selecttMix(mapM:string){
    // this.currentMapType = mapt;
    this.showOptionsDropdown = true;
    
    
  this.showSource = false;
  this.showMap = false;
  this.showTable = false;
  this.isVisible = false;
  this.showUnder15 = false;
  this.externalUrl = null;
  this.showMix = false;
  // this.showeast = false;
  //     this.showwest = false;
  setTimeout(() => {
    // Update the map type
    this.mapM = mapM;
    // Show the map after updating the map type
    this.showMix = true;
    
  }, 100); // 100 milliseconds delay
  }



  selectMap(mapType: "census" | "under15" | "combined" | "latestSourcing" | 
  "kala" | "basa" | "yadg" | "bija" | "kama" | "have" | "bela" | "chit" | "loka" | "goka" |
  "sham" | "hubb" | "shah" | "rane" | "darb" | "sakr" | "phul" | "runn" | "beni" | "sahe" | 
  "rose" | "sheo" | "kant" | "sita" | "sama"| "hath" | "jale" | "kitt"|
  "shiv" | "gora" | "chau" | "tund" | "alig" | "ikau" | "khad"  | "capt" | 
   "tara" | "maho" | "nich" | "kira" | "mix" ) {
  // Hide the map with a small delay
  this.currentMapType = mapType;
  this.showSource = false;
  this.showTable = false;
  this.showUnder15 = false;
 this.isVisible = false;
 this.showeast = false;
      this.showwest = false;
    this.showOptionsDropdown = true;
    this.isVisible = false;
    this.showMix = false;
    
  this.showMap = false;
  this.showUnder15  =false;
  this.externalUrl = null;
  setTimeout(() => {
    // Update the map type
    this.mapType = mapType;
    // Show the map after updating the map type
    this.showMap = true;
  }, 100); // 100 milliseconds delay
}

toggleerror():void{
  this.show_error = !this.show_error;
}
runScripts() {
  this.isLoading = true;
  this.runPythonScripts().subscribe({
    next: response => {
      console.log('Response:', response);
      this.scriptOutput = response;
      this.isLoading = false;
    },
    error: error => {
      console.error('Failed to execute scripts', error);
      this.scriptOutput = 'Error: ' + error.statusText;
      this.isLoading = false;
    }
  });
}






  
  
  
  
  
  
}
