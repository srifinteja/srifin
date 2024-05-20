import { AfterViewInit, Component, OnInit,Input, OnChanges, SimpleChanges,Injector } from '@angular/core';
import Map from 'ol/Map';
import View from 'ol/View';
import TileLayer from 'ol/layer/Tile';
import OSM from 'ol/source/OSM';
import { CensusData, Combined, LatestSourcing, MapTypeConfig, Mapdata, Radardata, Under15, mixData, negativeMaps } from './census-data';
import { HttpClient } from '@angular/common/http';
import { Observable, sequenceEqual } from 'rxjs';
import VectorSource from 'ol/source/Vector';
import { Feature } from 'ol';
import { Point } from 'ol/geom';
import { fromLonLat } from 'ol/proj';
import VectorLayer from 'ol/layer/Vector';
import Icon from 'ol/style/Icon';
import { Circle } from 'ol/geom';
import { Stroke, Style } from 'ol/style';
import { LayerVisibilityService } from '../color-layer-service';
import { transform } from 'ol/proj';
import GeoJSON from 'ol/format/GeoJSON';
import Fill from 'ol/style/Fill';
import Geometry from 'ol/geom/Geometry';
import { Conditional } from '@angular/compiler';
import { defaults as defaultControls } from 'ol/control';
import { forkJoin } from 'rxjs';
import { map } from 'rxjs/operators';
import { mixinColor } from '@angular/material/core';
import { AppComponent } from '../app.component';
interface MapComponentMethods {
  [methodName: string]: (data: any) => void;
}
interface URCounts {
  Rural: number;
  Urban: number;
}
interface FilterResult {
  unique:number,
  urCounts:URCounts,
  condition: string;
  uniqueCensusCodeCount: number;
  totalHouseholds: number;
  allowedAndCenterCount:number;
  notAllowedAndCenterCount:number;
  totalapp:number;
  totaldisb:number;
  conddisb:number;
  countFlag:number;
}
interface FilterIcons{

}

@Component({
  selector: 'app-map',
  templateUrl: './map.component.html',
  styleUrls: ['./map.component.css']
})
export class MapComponent implements OnInit,AfterViewInit,OnChanges {
  map!: Map;
  radius: number = 15000; 
  private vectorLayer: VectorLayer<VectorSource<Feature<Geometry>>> | null = null;
  private circleLayer: VectorLayer<VectorSource<Feature<Geometry>>> | null = null;
  selectedCensusData: CensusData | null = null;
  selectedUnder15Data: Under15 | null = null;
  selectedCombined15Data: Combined | null = null;
  selectedMapdata: Mapdata |null = null;
  selectedMixdata: mixData |null = null;
  selectedbeni_15:Under15|null = null;
  selecteddarb_15:Under15|null = null;
  selectedkant_15:Under15|null = null;
  selectedphul_15:Under15|null = null;
  selectedradar:Radardata|null = null;
  selectedrose_15:Under15|null = null;
  selectedrunn_15:Under15|null = null;
  selectedsahe_15:Under15|null = null;
  selectedsakr_15:Under15|null = null;
  // New property to hold either of the two properties
  currentSelectedData: any;
  selectedData:any;
  selectedLatestSourcing : LatestSourcing |null = null;
  showFilteredPoints: boolean = false; 
  data: any[] = [];
  filterResults: FilterResult[] = [];
  iconResults:FilterIcons[] = [];
  redLayer!: VectorLayer<VectorSource<Feature<Point>>>;
  greenLayer!: VectorLayer<VectorSource<Feature<Point>>>;
  xLayer!: VectorLayer<VectorSource<Feature<Point>>>;
  navyLayer!: VectorLayer<VectorSource<Feature<Point>>>;
  notAllowedLayer!: VectorLayer<VectorSource<Feature<Point>>>;
  missed!: VectorLayer<VectorSource<Feature<Point>>>;
  redLayer_allowed!: VectorLayer<VectorSource<Feature<Point>>>;
  greenLayer_allowed!: VectorLayer<VectorSource<Feature<Point>>>;
  xLayer_allowed!: VectorLayer<VectorSource<Feature<Point>>>;
  navyLayer_allowed!: VectorLayer<VectorSource<Feature<Point>>>;
  notAllowedLayer_allowed!: VectorLayer<VectorSource<Feature<Point>>>;
  redLayer_notallowed!: VectorLayer<VectorSource<Feature<Point>>>;
  greenLayer_notallowed!: VectorLayer<VectorSource<Feature<Point>>>;
  xLayer_notallowed!: VectorLayer<VectorSource<Feature<Point>>>;
  navyLayer_notallowed!: VectorLayer<VectorSource<Feature<Point>>>;
  notAllowedLayer_unexplored!: VectorLayer<VectorSource<Feature<Point>>>;
  redLayer_unexplored!: VectorLayer<VectorSource<Feature<Point>>>;
  greenLayer_unexplored!: VectorLayer<VectorSource<Feature<Point>>>;
  xLayer_unexplored!: VectorLayer<VectorSource<Feature<Point>>>;
  navyLayer_unexplored!: VectorLayer<VectorSource<Feature<Point>>>;
  notAllowedLayer_notallowed!: VectorLayer<VectorSource<Feature<Point>>>;
  missed1!: VectorLayer<VectorSource<Feature<Point>>>;
  allowedVisible = true;
notAllowedVisible = true;
unexploredVisible = true;

 darbcenterCoords: [number, number] = [85.9092286, 26.1705652];
 sakrcenterCoords: [number, number] = [86.0691029, 26.2034595];
 phulcenterCoords: [number, number] = [86.494003, 26.35992];
 runncenterCoords: [number, number] = [85.5018342, 26.3863901];
 benicenterCoords: [number, number] = [86.149654,26.061786];
 sahecenterCoords: [number, number] = [84.925219,26.302396];
 rosecenterCoords: [number, number] = [86.030598, 25.751524];
 sheocenterCoords: [number, number] = [85.2969007, 26.5115238];
 kantcenterCoords: [number, number] = [85.294562,26.21164];
 sitacenterCoords: [number, number] = [85.526382, 26.609735];
 samacenterCoords: [number, number] = [85.794196, 25.868067];


 kalacenterCoords: [number, number] = [76.862661,17.335377];
 basacenterCoords: [number, number] = [76.9404527,17.845656];
 yadgcenterCoords: [number, number] = [77.142486,16.748404];
 bijacenterCoords: [number, number] = [75.717539,16.802997];
 kamacenterCoords: [number, number] = [76.97595912,17.57170152];
 havecenterCoords: [number, number] = [75.393702,14.805786];
 belacenterCoords: [number, number] = [74.5489064,15.8869478];
 chitcenterCoords: [number, number] = [77.21511,17.69763];
 lokacenterCoords: [number, number] = [75.236837,16.161042];
 gokacenterCoords: [number, number] = [74.814176,16.10792];
 shamcenterCoords: [number, number] = [75.903002,14.447667];
 hubbcenterCoords: [number, number] = [75.072685,15.392705];
 shahcenterCoords: [number, number] = [76.83125,16.71365];
 ranecenterCoords: [number, number] = [75.63627,14.607483];
kittcenterCoords:[number,number] = [74.7704604,15.5932899];

 hathcenterCoords: [number, number] = [78.0613381,27.5695990];
 jalecenterCoords: [number, number] = [78.2947265,27.466723];
 shivcenterCoords: [number, number] = [82.9498766,25.3526766];
 goracenterCoords: [number, number] = [83.3876034,26.7348618,];
 chaucenterCoords: [number, number] = [83.5930928,26.6389515];
 tundcenterCoords: [number, number] = [78.230427,27.227812];
 aligcenterCoords: [number, number] = [78.1135004,27.9150648];
 ikaucenterCoords: [number, number] = [81.974199,27.526017];
 khadcenterCoords: [number, number] = [83.873463,27.175883];
 captcenterCoords: [number, number] = [83.711337,26.929438];
 taracenterCoords: [number, number] = [81.993151,26.94627];
 mahocenterCoords: [number, number] = [79.87318,25.30184];
 nichcenterCoords: [number, number] = [83.732047,27.309857];
 kiracenterCoords: [number, number] = [77.783291,27.1392655];
 
 sourceMap: { [key: string]: string } = {
  darb_Source: "Darbhanga",
  sakr_Source: "Sakri",
  phul_Source: "Phulparas",
  runn_Source: "Runnisaidpur",
  beni_Source: "Benipur",
  sahe_Source: "Sahebganj",
  rose_Source: "Rosera",
  sheo_Source: "Sheohar",
  kant_Source: "Kanti",
  sita_Source: "Sitamarhi",
  sama_Source: "Samastipur",
  kala_Source: "Kalaburgi",
  basa_Source: "Basavakalyan",
  yadg_Source: "Yadgir",
  bija_Source: "Bijapur",
  kama_Source: "Kamalapur",
  have_Source: "Haveri",
  bela_Source: "Belagavi",
  chit_Source: "Chitguppa",
  loka_Source: "Lokapur",
  goka_Source: "Gokak",
  sham_Source: "Shamanur",
  hubb_Source: "Hubbali",
  shah_Source: "Shahpur",
  rane_Source: "Ranebennur",
  hath_Source: "Hathras",
  jale_Source: "Jalesar",
  shiv_Source: "Shivpur",
  gora_Source: "Gorakhpur",
  chau_Source: "Chauri Chaura",
  tund_Source: "Tundla",
  alig_Source: "Aligarh",
  ikau_Source: "Ikauna",
  khad_Source: "Khadda",
  capt_Source: "Captainganj",
  tara_Source:"Tarabganj",
  maho_Source:"Mahoba",
  nich_Source:"Nichlaul",
  kira_Source:"Kiraoli",
  kitt_Source:"Kittur"
  
  
};
  @Input() mapType: "census" | "under15" | "combined" | "latestSourcing" | 
  "kala" | "basa" | "yadg" | "bija" | "kama" | "have" | "bela" | "chit" | "loka" | "goka" |
  "sham" | "hubb" | "shah" | "rane" | "darb" | "sakr" | "phul" | "runn" | "beni" | "sahe" | 
  "rose" | "sheo" | "kant" | "sita" | "sama" |"hath" |  "jale" | "kitt"|
   "shiv" | "gora" | "chau" | "tund" | "alig" | "ikau" | "khad" | "capt" | 
  "tara" | "maho" | "nich" | "kira" | "mix" |null
  ;

// In MapComponent
@Input() mapt: string | null = null;

@Input() mapS:string |null = null;
@Input() mapM:string |null = null;

// Method or getter to access the coordinates dynamically
private get centerCoordsMap(): { [key: string]: [number, number] } {
  return {
    darbSource: this.darbcenterCoords,
    sakrSource: this.sakrcenterCoords,
    phulSource: this.phulcenterCoords,
    runnSource: this.runncenterCoords,
    beniSource:this.benicenterCoords,
    saheSource: this.sahecenterCoords,
    roseSource:this.rosecenterCoords,
    sheoSource:this.sheocenterCoords,
    kantSource: this.kantcenterCoords,
    sitaSource: this.sitacenterCoords,
    samaSource:this.samacenterCoords,
    kalaSource: this.kalacenterCoords,
    basaSource:this.basacenterCoords,
    yadgSource: this.yadgcenterCoords,
    bijaSource:this.bijacenterCoords,
    kamaSource: this.kamacenterCoords,
    haveSource: this.havecenterCoords,
    belaSource:this.belacenterCoords,
    chitSource:this.chitcenterCoords,
    lokaSource:this.lokacenterCoords,
    gokaSource:this.gokacenterCoords,
    shamSource:this.shamcenterCoords,
    hubbSource:this.hubbcenterCoords,
    shahSource:this.shahcenterCoords,
    raneSource:this.ranecenterCoords,
    hathSource:this.hathcenterCoords,
    jaleSource:this.jalecenterCoords,
    shivSource:this.shivcenterCoords,
    goraSource:this.goracenterCoords,
    chauSource:this.chaucenterCoords,
    tundSource:this.tundcenterCoords,
    aligSource:this.aligcenterCoords,
    ikauSource:this.ikaucenterCoords,
    khadSource:this.khadcenterCoords,
    captSource:this.captcenterCoords,
    taraSource:this.taracenterCoords,
    mahoSource:this.mahocenterCoords,
    nichSource:this.nichcenterCoords,
    kiraSource:this.kiracenterCoords,
    kittSource:this.kittcenterCoords


  };
}
  constructor(
    private http: HttpClient,
    private layerVisibilityService: LayerVisibilityService,
    private injector:Injector
    
  ) {
    this.mapType = null;
    
  }
  ngOnInit(): void {
   this.initializeMap();
   this.triggerDataToMap();
   this.triggerMix();
   this.triggerSourceMap();
   const features = Object.values(this.centerCoordsMap).map(coords => {
    return new Feature({
      geometry: new Point(fromLonLat(coords)),
    });
  });
  
  // Create a vector source with features
  const vectorSource = new VectorSource({
    features: features // Add the prepared features
  });

  // Assuming createIconStyle is a method that returns an ol/style/Style object
  const iconStyle = this.createIconStyle('assets/home.png');

  // Create a vector layer using the vector source
  const vectorLayer = new VectorLayer({
    source: vectorSource,
    style: iconStyle // Set the style for the layer
  });

  // Add the vector layer to the map
  this.map.addLayer(vectorLayer);
  
   if(this.mapM!=null){
    this.getkaMapData().subscribe(mapData=>{
      this.data = mapData;
    const missedFeatures: Feature<Point>[] = [];
    mapData.forEach(item => {
      let imageUrl: string = '';
      const geometry = new Point(fromLonLat([item.longitude, item.latitude]));
  
        imageUrl = 'assets/pink.png';
        missedFeatures.push(new Feature({
          geometry: geometry,
          properties: {
            Radardata: item
          }
        }));
      });
      const missed = new VectorSource({features : missedFeatures}); 
      const missedLayer = new VectorLayer({ source: missed });
      const style55 = this.createIconStyle('assets/pink.png');
    missedLayer.setStyle(style55);
    this.map.addLayer(missedLayer);
    
    // missedLayer.setZIndex(zIndexPoints);
    });
    this.getupMapData().subscribe(mapData=>{
      this.data = mapData;
      const missedFeatures: Feature<Point>[] = [];
      mapData.forEach(item => {
        let imageUrl: string = '';
        const geometry = new Point(fromLonLat([item.longitude, item.latitude]));
    
          imageUrl = 'assets/pink.png';
          missedFeatures.push(new Feature({
            geometry: geometry,
            properties: {
              Radardata: item
            }
          }));
        });
        const missed = new VectorSource({features : missedFeatures}); 
        const missedLayer = new VectorLayer({ source: missed });
        const style55 = this.createIconStyle('assets/pink.png');
      missedLayer.setStyle(style55);
      this.map.addLayer(missedLayer);
      // missedLayer.setZIndex(zIndexPoints);
      });
      this.getbiharMapData().subscribe(mapData=>{
        this.data = mapData;
        const missedFeatures: Feature<Point>[] = [];
        mapData.forEach(item => {
          let imageUrl: string = '';
          const geometry = new Point(fromLonLat([item.longitude, item.latitude]));
      
            imageUrl = 'assets/pink.png';
            missedFeatures.push(new Feature({
              geometry: geometry,
              properties: {
                Radardata: item
              }
            }));
          });
          const missed = new VectorSource({features : missedFeatures}); 
          const missedLayer = new VectorLayer({ source: missed });
          const style55 = this.createIconStyle('assets/pink.png');
        missedLayer.setStyle(style55);
        this.map.addLayer(missedLayer);
        // missedLayer.setZIndex(zIndexPoints);
        });
  }

  
  










  
}
public triggerMix(): void {
  if (this.mapM != null) {
    const baseKey = this.mapM.split('_')[0];
    const sourceKey = baseKey + "Source"; // Keys like "darbSource"
    const sourceeKey = baseKey + "_Source";
    const centerCoords = this.centerCoordsMap[sourceKey];
    const x = this.sourceMap[sourceeKey];
    this.allowedVisible = true;
    this.notAllowedVisible = true;
    this.unexploredVisible = true;
    // Combine requests to fetch both sets of data
    forkJoin({
      mixData: this.getMixData(x),
      
      biharData: this.getbiharMapData(),
      updata: this.getupMapData(),
      kadata:this.getkaMapData()

    }).pipe(
      map(results => {
        // Combine both datasets before filtering
        const combinedData = [...results.mixData, ...results.biharData, ...results.updata,...results.kadata];
      
        return this.filterDataByRadius(combinedData, centerCoords);
      })
    ).subscribe(filteredData => {
      // Process the filtered data that now contains both mixData and biharData
      this.processData(filteredData,centerCoords);
    });
  }
}

// Generic filter function assuming data items contain latMinBoundCentroid, longMinBoundCentroid or equivalent
private filterDataByRadius(data: any[], centerCoords: any): any[] {
  return data.filter(item => {
    // Adapt these property accesses based on your actual data structure
    const lat = item.latMinBoundCentroid || item.latitude;
    const lon = item.longMinBoundCentroid || item.longitude;
    
    
    const distance = this.calculateDistance(centerCoords[1], centerCoords[0], lat, lon);
    return distance <= this.radius;
  });
}
  private processData(data: any[], centerCoords: [number, number]): void {
    var count = 0;
    const urCounts = { Rural: 0, Urban: 0 };
    data.forEach(item => {
      if(item.ur === 'Urban'){
      count++;
      
      }
      const urKey = item.ur as 'Rural' | 'Urban';
      if (urCounts.hasOwnProperty(urKey)) {
        ++urCounts[urKey];
      }
      else{
        
      }
    });
  
    const filteredUnique = new Set(data.map(item => item.censuscode2011));
    const uniq = filteredUnique.size;
    
    const conditions = [
      { visited: "Visited", catStatus: "Allowed" },
      { visited: "Visited", catStatus: "Not_Allowed" },
      { visited: "Yet-To-Visit", catStatus: "Allowed" },
      { visited: "Yet-To-Visit", catStatus: "Not_Allowed" },
     
    ];
    const temp = [
      {visited:"Yet-To-Visit",catStatus:"Allowed"}
    ];
   
    
    let allowedAndCenterExistsCount = 0;
    let notAllowedAndCenterExistsCount = 0;
    let totalLoanApplications = 0;
    let totalDisbursed = 0;
  
    const flagsToCheck = ['Ring Leader', 'Negative Area', 'External Inciter', 'Risky Area'];

// Set to track unique [latitude, longitude] pairs
const uniqueLocations = new Set();

const filteredData = data.filter(item => {
    const locationKey = `${item.latitude},${item.longitude}`; // Create a unique key based on latitude and longitude
    if (flagsToCheck.includes(item.flag) && !uniqueLocations.has(locationKey)) {
        uniqueLocations.add(locationKey);
        return true; // Include this item in the filtered results
    }
    return false; // Exclude if not matching the flags or if already seen
});

const countOfDataWithFlag = filteredData.length;

const t = data.filter(item=>
  item.visited === 'Yet-To-Visit' && item.catStatus === 'Allowed'
);
const tb = t.reduce((sum, item) => sum + item.disbursed, 0);


    this.filterResults = conditions.map(condition => {
      const conditionData = data.filter(item => 
        item.visited === condition.visited && item.catStatus === condition.catStatus
      );
      
      // this.filt = icons.map(condition => {
      //   const conditionData = data.filter(item => 
      //     item.visited === condition.visited && item.catStatus === condition.catStatus && item.center === condition.center
      //   );
      const uniqueCensusCodeCount = new Set(conditionData.map(item => item.censuscode2011)).size;
      const totalHouseholds = conditionData.reduce((acc, item) => acc + (item.houseHolds || 0), 0);
      const conditionDisbursed = conditionData.reduce((acc, item) => acc + (item.disbursed || 0), 0); // Calculate disbursed count for this condition
      
      if (condition.catStatus === "Allowed") {
        allowedAndCenterExistsCount += conditionData.filter(item => item.center === "Center_Exists").length;
      } else if (condition.catStatus === "Not_Allowed") {
        notAllowedAndCenterExistsCount += conditionData.filter(item => item.center === "Center_Exists").length;
      }
      
      conditionData.forEach(item => {
        totalLoanApplications += item.loanApps || 0;
        totalDisbursed += item.disbursed || 0;
      });
  // Additional processing...
  this.getupMapData().subscribe(mapData => {
    this.addMixDataToMap(data, mapData, centerCoords);
});
// this.getkaMapData().subscribe(mapData => {
//   this.addMixDataToMap(data, mapData, centerCoords);
// });
// this.getbiharMapData().subscribe(mapData => {
//   this.addMixDataToMap(data, mapData, centerCoords);
// });
      return {
        unique: uniq-1,
        urCounts,
        condition: `${condition.visited}, ${condition.catStatus}`,
        uniqueCensusCodeCount,
        totalHouseholds,
        allowedAndCenterCount: allowedAndCenterExistsCount,
        notAllowedAndCenterCount: notAllowedAndCenterExistsCount,
        totalapp: totalLoanApplications,
        totaldisb: totalDisbursed+tb,
        conddisb:conditionDisbursed,
        countFlag:countOfDataWithFlag
      };
        
    });
     // Populate iconResults
  //    this.iconResults = icons.map(icon => {
      
  //     const iconData = data.filter(item =>  
  //         item.visited === icon.visited && item.catStatus === icon.catStatus && item.center === icon.center
  //     );
      
   
  

  //     return iconData.length;
  // });
  }
    

public triggerSourceMap():void{
  if (this.mapS != null) {
    // Assuming this.mapS value is like "darb_Source", extract "darb" to match keys in centerCoordsMap
    const sourceKey = this.mapS.split('_')[0] + "Source"; // Convert to match your keys like "darbSource"
    const centerCoords = this.centerCoordsMap[sourceKey];
    const x = this.sourceMap[this.mapS];
    if (centerCoords) {
      // Here, you'd fetch data using a friendly name derived from this.mapS or another mapping
      // For simplicity, let's just use sourceKey directly if it matches your data fetching keys
      this.getSourceData(x).subscribe((data: any) => {
        
        this.data = data;
        // Use your method to add data to the map
        this.addSourceDataToMap(sourceKey, centerCoords, data);
      });
    } else {
      console.error(`Coordinates not found for source key: ${sourceKey}`);
    }
  }
}
// Use the mapping, making sure to handle potential undefined values
public triggerDataToMap(): void {
  if (this.mapt != null) {
    // Assuming this.mapS value is like "darb_Source", extract "darb" to match keys in centerCoordsMap
    const sourceKey = this.mapt.split('_')[0] + "Source"; // Convert to match your keys like "darbSource"
    
    const centerCoords = this.centerCoordsMap[sourceKey];
    const sourceeKey = this.mapt.split('_')[0] + "_Source";
    
    const x = this.sourceMap[sourceeKey];
    
    if (centerCoords) {
      // Here, you'd fetch data using a friendly name derived from this.mapS or another mapping
      // For simplicity, let's just use sourceKey directly if it matches your data fetching keys
      this.getUnder15Data(x).subscribe((data: any) => {
        
        this.data = data;
        // Use your method to add data to the map
        this.addDataToMap(data, sourceKey+'15', item => item.deep_status === 'Not Allowed' ? 'assets/red.png' : 'assets/green1.png',centerCoords);
      });
    } else {
      console.error(`Coordinates not found for source key: ${sourceKey}`);
    }
  }
  }

  ngOnChanges(changes: SimpleChanges): void {
    // This method will run when any input property changes
    if (changes['mapt']) {
      const currentValue = changes['mapt'].currentValue;
      if (currentValue !== null) {
        

        // Perform actions with currentValue
      }
    }
  }
  getdarbSourceData(): Observable<LatestSourcing[]> {
    return this.http.get<LatestSourcing[]>('http://localhost:8080/api/census/darbSource');
  }
  getsakrSourceData(): Observable<LatestSourcing[]> {
    return this.http.get<LatestSourcing[]>('http://localhost:8080/api/census/sakrSource');
  }
  getphulSourceData(): Observable<LatestSourcing[]> {
    return this.http.get<LatestSourcing[]>('http://localhost:8080/api/census/phulSource');
  }
  getrunnSourceData(): Observable<LatestSourcing[]> {
    return this.http.get<LatestSourcing[]>('http://localhost:8080/api/census/runnSource');
  }
  getbeniSourceData(): Observable<LatestSourcing[]> {
    return this.http.get<LatestSourcing[]>('http://localhost:8080/api/census/beniSource');
  }
  getsaheSourceData(): Observable<LatestSourcing[]> {
    return this.http.get<LatestSourcing[]>('http://localhost:8080/api/census/saheSource');
  }
  getroseSourceData(): Observable<LatestSourcing[]> {
    return this.http.get<LatestSourcing[]>('http://localhost:8080/api/census/roseSource');
  }
  getsheoSourceData(): Observable<LatestSourcing[]> {
    return this.http.get<LatestSourcing[]>('http://localhost:8080/api/census/sheoSource');
  }
  getkantSourceData(): Observable<LatestSourcing[]> {
    return this.http.get<LatestSourcing[]>('http://localhost:8080/api/census/kantSource');
  }
  getsitaSourceData(): Observable<LatestSourcing[]> {
    return this.http.get<LatestSourcing[]>('http://localhost:8080/api/census/sitaSource');
  }
  getsamaSourceData(): Observable<LatestSourcing[]> {
    return this.http.get<LatestSourcing[]>('http://localhost:8080/api/census/samaSource');
  }

  getNegative_up(): Observable<negativeMaps[]> {
    return this.http.get<negativeMaps[]>('http://localhost:8080/api/census/up_negativeData');
  }
  getNegative_ka(): Observable<negativeMaps[]> {
    return this.http.get<negativeMaps[]>('http://localhost:8080/api/census/ka_negativeData');
  }
  getNegative_br(): Observable<negativeMaps[]> {
    return this.http.get<negativeMaps[]>('http://localhost:8080/api/census/br_negativeData');
  }
  private baseUrl: string = 'http://localhost:8080/api/census/';
  getUnder15Data(cityName: string): Observable<Under15[]> {
    const url = `${this.baseUrl}${cityName}Under15`;
    return this.http.get<Under15[]>(url);
  }
 

  private baseUrlSource: string = 'http://localhost:8080/api/census/';
  getSourceData(cityName: string): Observable<LatestSourcing[]> {
    const url = `${this.baseUrlSource}${cityName}Source`;
    return this.http.get<LatestSourcing[]>(url);
  }

  // http://localhost:8080/api/census/mixData/Sakri
  private baseUrlMix: string = 'http://localhost:8080/api/census/mixData/';
  getMixData(cityName: string): Observable<mixData[]> {
    const url = `${this.baseUrlMix}${cityName}`;
      const observable = this.http.get<mixData[]>(url);
    // console.log(observable);
    return this.http.get<mixData[]>(url);
  }

// Generalized method to add a point to the map
addPointToMap(longitude: number, latitude: number, iconPath: string) {
  const feature = new Feature({
    geometry: new Point(fromLonLat([longitude, latitude])),
  });
  feature.setStyle(this.createIconStyle(iconPath));
  const vectorSource = new VectorSource({ features: [feature] });
  const vectorLayer = new VectorLayer({ source: vectorSource });
  this.map.addLayer(vectorLayer);
  this.map.getView().animate({
    center: fromLonLat([longitude, latitude]),
    duration: 2000, // Duration of the animation in milliseconds
    zoom: 10 // Adjust zoom level as needed
  });
}

  // In your color conversion service or within an Angular component

convertColorNameToRGBA(colorName: string, opacity: number = 0.5): string {
  const colors: { [key: string]: string } = {
    red: '255,0,0',
    green: '0,128,0',
    blue: '0,0,255',
    // add more colors as needed
  };

  // Convert the color name to lower case to ensure case-insensitive matching
  const rgb = colors[colorName.toLowerCase()] || '0,0,0'; // Default to black if not found
  return `rgba(${rgb},${opacity})`;
}


  private initializeMap(): void {
    this.map = new Map({
      target: 'map',
      layers: [
        new TileLayer({
          source: new OSM()
        })
      ],
      controls: defaultControls({
        attribution: false  // Exclude the Attribution control
      }),
      view: new View({
        center: fromLonLat([82.9560, 25.3176]), // Coordinates of Varanasi
        zoom: 11 
      })
    });
    
}
fetchGeoJSONData(censuscode: string, color: string): void {
  this.http.get<any>('http://localhost:8080/api/census/text-file').subscribe(data => {
    if (data) {
      const geojsonFormat = new GeoJSON();
      const allFeatures: Feature<Geometry>[] = geojsonFormat.readFeatures(data, {
        dataProjection: 'EPSG:4326',
        featureProjection: 'EPSG:3857'
      }) as Feature<Geometry>[]; // Explicitly type as Feature<Geometry>[]
      
      // Filter for features with a specific censuscode
      // const specificCensusCode = "801235"; // Define the specific censuscode you're interested in
      const filteredFeatures = allFeatures.filter(feature => {
        
        return feature.get('censuscode2011') === censuscode;
      });
      
      if (filteredFeatures.length > 0) {
        // If there are features with the specified censuscode
        // const color = 'rgba(255, 0, 0, 0.5)'; // Define the color for these features

        const vectorSource = new VectorSource({
          features: filteredFeatures // Use the filtered features
        });

        const vectorLayer = new VectorLayer({
          source: vectorSource,
          style: new Style({
            stroke: new Stroke({
              color: 'black',
              width: 3
            }),
            fill: new Fill({
              color: color // Using the same color for fill
            }),
          })
        });

        this.map.addLayer(vectorLayer);
      } else {
        console.warn(`No features found with censuscode ${censuscode}`);
      }
    } else {
      console.error('No data received from the API');
    }
  }, error => {
    console.error('Error fetching GeoJSON data:', error);
  });
}


 
  ngAfterViewInit(): void {
    setTimeout(() => this.map.updateSize(), 0);
    this.map.on('singleclick', (event) => {
      const clickedFeatures: Feature[] = [];
      this.map.forEachFeatureAtPixel(event.pixel, (feature) => {
        if (feature instanceof Feature) {
          this.handleFeatureClick(feature);
        }
      });
    });
    setTimeout(() => this.map.updateSize(), 0);

  }

    

  private handleFeatureClick(feature: Feature): void {
    // if (this.mapType === "census") {
    //   const censusData: CensusData = feature.get('censusData');
    //   if (censusData) {
    //     this.selectedCensusData = censusData;
    //   }
    // } else if (this.mapType === "under15") {
  //     const under15Data: Under15 = feature.get('under15');
  


      
  //     if (under15Data) {
  //       this.selectedUnder15Data = under15Data;
  //       this.updateCurrentSelectedData();
  //     }
  //   } else if (this.mapType === "combined") {
      
  //     const mapData:Mapdata = feature.getProperties()['properties']['combined'];
  //     if(mapData && mapData['flag']){
  //       this.selectedMapdata = mapData;
  //     }
  //     else{
  //     const combined: Combined = feature.getProperties()['properties']['combined'];
  //     if (combined) {
  //       this.selectedCombined15Data = combined;
  //     }
  //   }
  // }
  // else if(this.mapType === "latestSourcing"){
  //   // Call getProperties() method to actually retrieve the properties
  //   const properties = feature['values_'];
    
  //   // Assuming properties contain a nested object that matches the LatestSourcing structure
  //   // You might need to adjust the access depending on how your data is structured
  //   const latest: LatestSourcing = properties['latestSourcing']; // Adjust this line based on your actual data structure
    
    
  
  //   if(properties){
  //     this.selectedLatestSourcing = properties;
  //   }
  //  
  // }
  //  if(this.mapType === "mix"){
  //   // Assuming 'feature' is the variable holding your feature data
  //   const properties = feature.getProperties()['properties']; // Gets the entire properties object
  //   this.selectedMixdata = properties['mixData']; // Accesses mixData directly
    
  // }
   if(this.mapt){
    // Assuming this code is inside a method of your component class
const maptToPropKeyBase = this.mapt.match(/^.{4}/); // Extracts the first 4 characters of this.mapt
if (maptToPropKeyBase) {
  const propKey = `${maptToPropKeyBase}_15`; // Constructs the key dynamically
  const dataSourceKey = `${maptToPropKeyBase}Source15`; // Constructs the dataSourceKey dynamically
  const prop = feature.getProperties()[dataSourceKey];
  
  if (prop) {
    

    // Dynamically assign the prop to selectedData
    this.selectedData = prop;
    this.updateCurrentSelectedData();
  } else {
    console.error("Invalid dataSourceKey:", dataSourceKey);
  }
} else {
  console.error("Invalid mapt value or format:", this.mapt);
}

  }
if(this.mapS){
  const properties = feature.getProperties()['darbSource'];
  

      // Assuming this code is inside a method of your component class
const mapSToPropKeyBase = this.mapS.match(/^.{4}/); // Extracts the first 4 characters of this.mapt
if (mapSToPropKeyBase) {
  const propKey = `${mapSToPropKeyBase}_Source`; // Constructs the key dynamically
  const dataSourceKey = `${mapSToPropKeyBase}Source`; // Constructs the dataSourceKey dynamically
  const prop = feature.getProperties()[dataSourceKey];
  
  if (prop) {
    
    // Dynamically assign the prop to selectedData
    this.selectedSource = prop;
    this.updateCurrentSelectedSource();
  } else {
    console.error("Invalid dataSourceKey:", dataSourceKey);
  }
} else {
  console.error("Invalid mapt value or format:", this.mapt);
}

  }
if(this.mapM){
  const properties = feature.getProperties()['mixData'];
  
  const mapSToPropKeyBase = this.mapM.match(/^.{4}/); // Extracts the first 4 characters of this.mapt
  if (mapSToPropKeyBase) {
    const propKey = `${mapSToPropKeyBase}_Source`; // Constructs the key dynamically
    const dataSourceKey = `${mapSToPropKeyBase}Source`; // Constructs the dataSourceKey dynamically
    const prop = properties;
    
    if (prop) {
      
  
      // Dynamically assign the prop to selectedData
      this.selectedMix = prop;
      this.updateCurrentSelectedMix();
    } else {
      console.error("Invalid dataSourceKey:", dataSourceKey);
    }
  } else {
    console.error("Invalid mapt value or format:", this.mapt);
  }
  const proper = feature.getProperties()['properties']['Radardata'];
  this.selectedradar = proper;

}
  
  }
  selectedSource:any;
  latestSourcingData:any;
  selectedMix:any;
  MixData:any;
 // Method to update currentSelectedData based on your logic
 updateCurrentSelectedData() {
  // Example logic to update currentSelectedData
  this.currentSelectedData = this.selectedData;
}
updateCurrentSelectedSource() {
  // Example logic to update currentSelectedData
  this.latestSourcingData = this.selectedSource;
}
updateCurrentSelectedMix() {
  // Example logic to update currentSelectedData
  this.MixData = this.selectedMix;
}
 

  
  getCensusData(): Observable<CensusData[]> {
    return this.http.get<CensusData[]>('http://localhost:8080/api/census');
  }

  getCombinedData(): Observable<Combined[]> {
    return this.http.get<Combined[]>('http://localhost:8080/api/census/Combined');
  }

  getupMapData(): Observable<Mapdata[]> {
    return this.http.get<Mapdata[]>('http://localhost:8080/api/census/upMapdata');
  }
  getbiharMapData(): Observable<Mapdata[]> {
    return this.http.get<Mapdata[]>('http://localhost:8080/api/census/biharMapdata');
  }
  getkaMapData(): Observable<Mapdata[]> {
    return this.http.get<Mapdata[]>('http://localhost:8080/api/census/kaMapdata');
  }
  getmixData(): Observable<mixData[]> {
    
    return this.http.get<mixData[]>('http://localhost:8080/api/census/MixData');

  }
 
  getLatestSourcingData():Observable<LatestSourcing[]>{
    return this.http.get<LatestSourcing[]>('http://localhost:8080/api/census/latestSourcing');
  }
  private addDataToMap(data: any[], attribute: string, imageUrlCondition: (item: any) => string, centerCoords: [number, number]): void {
    const features = data.reduce((acc, item) => {
      const itemCoords = [item.long_min_bound_centroid || item.longMinBoundCentroid, item.lat_min_bound_centroid || item.latMinBoundCentroid];
      const distance = this.calculateDistance(centerCoords[1], centerCoords[0], itemCoords[1], itemCoords[0]);
    
      if (distance <= this.radius) {
        const imageUrl = imageUrlCondition(item);
        const geometry = new Point(fromLonLat(itemCoords));
        const feature = new Feature({ geometry: geometry });
        feature.set(attribute, item);
        feature.setStyle(this.createIconStyle(imageUrl));
        acc.push(feature); // Add the feature to the accumulator
      }
    
      return acc; // Return the accumulated features
    }, []);
    const vectorSource = new VectorSource({ features: features });
    const homeFeature = new Feature({ geometry: new Point(fromLonLat(centerCoords)) });
    homeFeature.setStyle(this.createIconStyle('assets/home.png'));
    vectorSource.addFeature(homeFeature);
  
    // Check if a vectorLayer already exists and if so, remove it
    if (this.vectorLayer) {
      this.map.removeLayer(this.vectorLayer);
    }
  
    // Create a new VectorLayer with the updated source
    this.vectorLayer = new VectorLayer({
      source: vectorSource
    });
  
    // Add the new or updated vectorLayer to the map
    this.map.addLayer(this.vectorLayer);
  // Add or update the circle representing the radius.
  this.addCircleToMap(centerCoords, this.radius);
    // Adjust the map view as needed
    this.map.setView(new View({
      center: fromLonLat(centerCoords),
      zoom: 11 // Adjust the zoom level based on your requirements
    }));
  }

private addCensusDataToMap(data: CensusData[]): void {
  const centerCoords: [number, number] = [82.9498766, 25.3526766];
  this.addDataToMap(data, 'censusData', item => item.visited === 'Yet_to_Visit' ? 'assets/red.png' : 'assets/x.png',centerCoords);
}



private addSourceDataToMap(source:string,sourceName: [number,number], data: LatestSourcing[]): void {
  
  // const centerCoords = this.sourceToCoords[sourceName];
  if (!sourceName) {
    console.error(`Coordinates for ${sourceName} not found.`);
    return;
  }
  this.addDataToMap(data, source, item => item.visited === 'Yet-To-Visit' ? 'assets/red.png' : 'assets/green1.png', sourceName);
}

private addCircleToMap(centerCoords: [number, number], radius: number): void {
  
    // If there's a previously added circle, remove it
    
    if (this.circleLayer) {
      this.map.removeLayer(this.circleLayer);
      // this.circleLayer = null;
    }
  const circleGeometry = new Circle(fromLonLat(centerCoords), radius);
  const circleFeature = new Feature({
    geometry: circleGeometry
  });

  circleFeature.setStyle(
    new Style({
      stroke: new Stroke({
        color: 'rgba(255, 0, 0, 0.6)',
        width: 2
      })
    })
  );

  const vectorSource = new VectorSource({
    features: [circleFeature]
  });

  // Directly assign the newly created layer to this.circleLayer
  this.circleLayer = new VectorLayer({
    source: vectorSource
  });

  // Now this.circleLayer is guaranteed to be defined
  this.map.addLayer(this.circleLayer);
}

// Utility function to calculate distance between two points in meters
private  calculateDistance(lat1: number, lon1: number, lat2: number, lon2: number): number {
  const R = 6371e3; // Earth radius in meters
  const φ1 = lat1 * Math.PI / 180;
  const φ2 = lat2 * Math.PI / 180;
  const Δφ = (lat2 - lat1) * Math.PI / 180;
  const Δλ = (lon2 - lon1) * Math.PI / 180;

  const a = Math.sin(Δφ / 2) * Math.sin(Δφ / 2) +
            Math.cos(φ1) * Math.cos(φ2) *
            Math.sin(Δλ / 2) * Math.sin(Δλ / 2);
  const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));

  return R * c; // Distance in meters
}



redLayerVisible: boolean = true
navyLayerVisible: boolean = true
greenLayerVisible: boolean = true
xLayerVisible: boolean = true
notallowedVisible: boolean = true
redLayerVisible_notallowed: boolean = true
navyLayerVisible_notallowed: boolean = true
greenLayerVisible_notallowed: boolean = true
xLayerVisible_notallowed: boolean = true
notallowedVisible_notallowed: boolean = true
redLayerVisible_unexp: boolean = true
navyLayerVisible_unexp: boolean = true
greenLayerVisible_unexp: boolean = true
xLayerVisible_unexp: boolean = true
notallowedVisible_unexp: boolean = true
// Method to toggle the visibility of the red layer
toggleRedLayerVisibility(): void {
  if (this.redLayer) {
    this.redLayer.setVisible(!this.redLayer.getVisible()); 
  }
   if(this.redLayer_allowed){
    
    this.redLayer_allowed.setVisible(!this.redLayer_allowed.getVisible()); 
  }
 
}
toggleRedLayer_alloed_visibility():void{
  if(this.redLayer_notallowed){
    
    this.redLayer_notallowed.setVisible(!this.redLayer_notallowed.getVisible()); 
  }
}
toggleRedLayer_unexplored_visibility():void{
  if(this.redLayer_unexplored){
    
    this.redLayer_unexplored.setVisible(!this.redLayer_unexplored.getVisible()); 
  }
}

// Method to toggle the visibility of the navy layer
togglenavyLayerVisibility(): void {
  if (this.navyLayer) {
    this.navyLayer.setVisible(!this.navyLayer.getVisible()); 
  }
  if(this.navyLayer_allowed){
    this.navyLayer_allowed.setVisible(!this.navyLayer_allowed.getVisible()); 
  }
 
 
}
togglenavy_notallowed():void{
  if(this.navyLayer_notallowed){
    this.navyLayer_notallowed.setVisible(!this.navyLayer_notallowed.getVisible()); 
  }
}
togglenavy_unexp():void{
  if(this.navyLayer_unexplored){
    this.navyLayer_unexplored.setVisible(!this.navyLayer_unexplored.getVisible()); 
  }
}

// Method to toggle the visibility of the green layer
togglegreenLayerVisibility(): void {
  if (this.greenLayer) {
    this.greenLayer.setVisible(!this.greenLayer.getVisible()); 
  }
  if(this.greenLayer_allowed){
    this.greenLayer_allowed.setVisible(!this.greenLayer_allowed.getVisible()); 
  }

}
togglegreen_notall():void{
if(this.greenLayer_notallowed){
    this.greenLayer_notallowed.setVisible(!this.greenLayer_notallowed.getVisible()); 
  }
}
togglegreen_unexp():void{
  if(this.greenLayer_unexplored){
    this.greenLayer_unexplored.setVisible(!this.greenLayer_unexplored.getVisible()); 
  }
  }
// Method to toggle the visibility of the green layer
togglexLayerVisibility(): void {
  if (this.xLayer) {
    this.xLayer.setVisible(!this.xLayer.getVisible()); 
  }
  if(this.xLayer_allowed){
    this.xLayer_allowed.setVisible(!this.xLayer_allowed.getVisible()); 
  }
  
}
togglexlayer_notllowed():void{
  if(this.xLayer_notallowed){
    this.xLayer_notallowed.setVisible(!this.xLayer_notallowed.getVisible()); 
  }
}

togglexunexp():void{
  if(this.xLayer_unexplored){
    this.xLayer_unexplored.setVisible(!this.xLayer_unexplored.getVisible()); 
  }
}


// Method to toggle the visibility of the green layer
togglenotAllowedLayerVisibility(): void {
  if (this.notAllowedLayer) {
    this.notAllowedLayer.setVisible(!this.notAllowedLayer.getVisible()); 
  }
  if (this.notAllowedLayer_allowed) {
    this.notAllowedLayer_allowed.setVisible(!this.notAllowedLayer_allowed.getVisible()); 
  }

}

togglenotallowed_notallowd():void{
  if (this.notAllowedLayer_notallowed) {
    this.notAllowedLayer_notallowed.setVisible(!this.notAllowedLayer_notallowed.getVisible()); 
  }
}

togglenotallwedd_unexp():void{
  if (this.notAllowedLayer_unexplored) {
    this.notAllowedLayer_unexplored.setVisible(!this.notAllowedLayer_unexplored.getVisible()); 
  }
}

maptodataLayerVisible: boolean = true

toggleMapdataLayerVisibility(): void {
  if (this.missed) {
    this.missed.setVisible(!this.missed.getVisible()); 
  }
}







maptodataLayerVisible_notallowed: boolean = true
maptodataLayerVisible_unexp: boolean = true

private addlatestDataToMap(data: LatestSourcing[], mapData: Mapdata[]): void {
  const centerCoords: [number, number] = [82.9498766, 25.3526766];
  const radius = 15000; // 15km in meters
const homeFeature = new Feature({
  geometry: new Point(fromLonLat([82.9498766, 25.3526766])),
});
homeFeature.setStyle(this.createIconStyle('assets/home.png'));
const homeVectorSource = new VectorSource({ features: [homeFeature] });
const homeVectorLayer = new VectorLayer({ source: homeVectorSource });
this.map.addLayer(homeVectorLayer);
  data.forEach(item => {
    let color = this.determineColor(item.jun23Cat,item.visited); // Implement this based on your logic
    let transcol = 'rgba(0,0,0,0)';
    this.fetchGeoJSONData(item.censuscode2011.toString(), transcol);

    

  });
}


private determineColor(jun23Cat: string, visited: string): string {
  // Your categorization logic here, returning 'green', 'red', 'blue', or 'pink'
  if(!jun23Cat|| jun23Cat.toLowerCase() === 'nan' || jun23Cat === '[]'){
    //pink unexplored
    return 'rgb(255, 192, 203,0.25)';//pink
  }
  const categories = jun23Cat.match(/\d+/g); // Extract numbers from the string

  
  
    // If there are no numbers and 'nan' is present, consider it as 'Unexplored'
    if (!categories && jun23Cat.includes('nan')) {
      return 'rgb(255, 192, 203,0.25)'; // pink Unexplored
    }
  
    // Assuming at least one category is present
    let hasAllowed = false;
    let hasNotAllowed = false;
  if(categories)
    categories.forEach(categ => {
      const num = parseInt(categ, 10);
      if (num <= 5) {
        hasAllowed = true;
      } else {
        hasNotAllowed = true;
      }
    });
  
    // Determine the color based on the conditions
    if (hasAllowed && !hasNotAllowed ) {
      if(visited==='Visited')
      return 'rgb(0, 255, 0,0.25)'; // green Allowed+visited
    else if(visited==='Yet-To-Visit')
    return 'rgb(0, 0, 255,0.25)';//blue

    } else if (!hasAllowed && hasNotAllowed) {
      if(visited==='Visited')
      return 'rgba(255, 0, 0, 0.25)'; // red-NotAllowed+visited
    else if(visited==='Yet-To-Visit')
    return 'rgb(255, 170, 51,0.25)'; //yellow
      // return 'red'; // Not Allowed
    } else if (hasAllowed) {
      return 'rgb(255, 192, 203,0.25)';  // pink Partially Allowed (has at least one allowed) r: 255, g: 192, b: 203
    }
  
    // Default to pink if none of the above conditions are met (for safety, though all cases should be covered)
    return 'rgb(255, 192, 203,0.25)'; //pink Unexplored
  
  


}




private createIconStyle(imageUrl: string): Style {
  return new Style({
    image: new Icon({
      anchor: [0.5, 1],
      scale: 0.16, // Adjust scale based on your icon's size to fit the map appropriately
      src: imageUrl
    })
  });
}


clearSelectedData(): void {
  
   if(this.mapM){
    this.MixData =  null;
    this.selectedradar = null;
  }
 
 
}
toggleAllowedVisibility(event: any) {
  this.allowedVisible = event.target.checked;
  this.toggleLayerVisibility('allowed', this.allowedVisible);
}

toggleNotAllowedVisibility(event: any) {
  this.notAllowedVisible = event.target.checked;
  this.toggleLayerVisibility('not_allowed', this.notAllowedVisible);
}

toggleUnexploredVisibility(event: any) {
  this.unexploredVisible = event.target.checked;
  this.toggleLayerVisibility('unexplored', this.unexploredVisible);
}

private toggleLayerVisibility(category: string, isVisible: boolean) {
  if (this.featureLayers && this.featureLayers[category]) {
    this.featureLayers[category].setVisible(isVisible);
  }
}


private featureLayers: { [key: string]: VectorLayer<VectorSource<Feature<Geometry>>>  } = {}; // To store references to feature layers

private addMixDataToMap(data: mixData[], mapData: Mapdata[], centerCoords: [number, number]): void {
  const transformedCenter = fromLonLat(centerCoords);
  
  this.map.getView().animate({ center: transformedCenter, zoom: 10, duration: 100 });
  const appComponent = this.injector.get(AppComponent); // Assuming AppComponent is injectable
  const routeLayer = appComponent.getRouteLayer();
  if (routeLayer) {
    this.map.removeLayer(routeLayer);
  }
  // Remove existing layers
  Object.values(this.featureLayers).forEach(layer => this.map.removeLayer(layer));
  this.featureLayers = {}; // Reset the layer references

  // Categorize and filter data
  const categories = ['allowed', 'not_allowed', 'unexplored']; // Define your categories
  categories.forEach(category => {
    const features = data
      .filter(item => this.meetsCriteria(item, category, centerCoords)) // Filter and categorize
      .map(item => this.createFeature(item)); // Create features
    
    if (features.length > 0) {
      // Create a new layer and add it to the map
      const vectorSource = new VectorSource({ features });
      const vectorLayer = new VectorLayer({ source: vectorSource });
      this.map.addLayer(vectorLayer);
      this.featureLayers[category] = vectorLayer; // Store the layer reference
    }
  });
  const homeFeature = new Feature({
  
    geometry: new Point(fromLonLat(centerCoords))
  });
  
  homeFeature.setStyle(this.createIconStyle('assets/home.png'));
  const homeVectorSource = new VectorSource({ features: [homeFeature] });
  const homeVectorLayer = new VectorLayer({ source: homeVectorSource });
  this.map.addLayer(homeVectorLayer); 
  this.addCircleToMap(centerCoords, this.radius);

  if (routeLayer) {
    console.log("hi");
    this.map.addLayer(routeLayer);
  }
  
  // Optionally, add other map setup here (e.g., addCircleToMap)
  
}
routeLayerVisible:boolean = true;
toggleRouteLayer(): void {
  const appComponent = this.injector.get(AppComponent); // Assuming AppComponent is injectable
  const routeLayer = appComponent.getRouteLayer();
  this.routeLayerVisible = !this.routeLayerVisible;
  if (routeLayer) {
    routeLayer.setVisible(this.routeLayerVisible);
  }
}
private meetsCriteria(item: mixData, category: string, centerCoords: [number, number]): boolean {
  // if(item.catStatus.toLowerCase()=='unexplored'){
  
  // }
  const distance = this.calculateDistance(centerCoords[1], centerCoords[0], item.latMinBoundCentroid, item.longMinBoundCentroid);
  // if(distance<=this.radius)
  
  return distance <= this.radius && item.catStatus.toLowerCase() === category;
}

private createFeature(item: mixData): Feature {
  const geometry = new Point(fromLonLat([item.longMinBoundCentroid, item.latMinBoundCentroid]));
  const feature = new Feature({ geometry });
  const imageUrl = this.getImageUrlBasedOnItem(item); // Implement this based on your logic
//  const imageUrl = 'assets/green.png';
feature.set('mixData', item);
  feature.setStyle(this.createIconStyle(imageUrl));
  return feature;
}


private getImageUrlBasedOnItem(item: mixData): string {
  // Example logic based on the 'visited', 'center', and 'catStatus' properties
  if (item.catStatus === 'Allowed') {
      if (item.visited === 'Visited' && item.center === 'No_Center') {
          return 'assets/red.png';
      } else if (item.visited === 'Visited' && item.center === 'Center_Exists') {
          return 'assets/green.png';
      } else if (item.visited === 'Yet-To-Visit' && item.center === 'No_Center') {
          return 'assets/x.png';
      } else if (item.visited === 'Yet-To-Visit' && item.center === 'Center_Exists') {
          return 'assets/navy.png';
      }
  } else if (item.catStatus === 'Not_Allowed') {
    if (item.visited === 'Visited' && item.center === 'No_Center') {
      return 'assets/red.png';
  } else if (item.visited === 'Visited' && item.center === 'Center_Exists') {
      return 'assets/green.png';
  } else if (item.visited === 'Yet-To-Visit' && item.center === 'No_Center') {
      return 'assets/x.png';
  } else if (item.visited === 'Yet-To-Visit' && item.center === 'Center_Exists') {
      return 'assets/navy.png';
  }
  } else if (item.catStatus === 'Unexplored') {
    if (item.visited === 'Visited' && item.center === 'No_Center') {
      return 'assets/red.png';
  } else if (item.visited === 'Visited' && item.center === 'Center_Exists') {
      return 'assets/green.png';
  } else if (item.visited === 'Yet-To-Visit' && item.center === 'No_Center') {
      return 'assets/x.png';
  } else if (item.visited === 'Yet-To-Visit' && item.center === 'Center_Exists') {
      return 'assets/navy.png';
  }
  }

  // Default icon if none of the above conditions are met
  return 'assets/default.png';
}



}
