
// src/app/models/census-data.model.ts

export interface CensusData {
    censusCode2011: string;
    village: string;
    pincode: string;
    district: string;
    state: string;
    totP2011: number;
    noHh2011: number;
    tru2011: string;
    latMinBoundCentroid: number;
    longMinBoundCentroid: number;
    finalCat: string;
    status: string;
    deepStatus: string;
    bDist: number;
    visited: string; // Consider using boolean if appropriate
  }
  

  export interface Under15 {
    censuscode2011: string;
    village: string;
    pincode: string;
    district: string;
    state: string;
    tot_p_2011: number;
    no_hh_2011: number;
    tru_2011: string;
    is_pc_in: string;
    lat_min_bound_centroid: number;
    long_min_bound_centroid: number;
    alpha_70_stat: string;
    poly_valid: string;
    Final_Cat: string;
    status: string;
    deep_stat: string;
    deep_status: string;
    b_dist: string;
  }
  
  export interface Combined {
    censusCode2011: string;
    village: string;
    pincode: string;
    district: string;
    state: string;
    totP2011: number;
    noHh2011: number;
    tru2011: string;
    latMinBoundCentroid: number;
    longMinBoundCentroid: number;
    alpha70Stat: string;
    polyValid: string;
    finalCat: string;
    status: string;
    deepStat: string;
    deepStatus: string;
    bDist: number;
    visited: string;
    center: string;
}
// src/app/models/latest-sourcing.ts
export interface negativeMaps {
  branch: string;
  latestApplication: string;
  pincode: string;
  jun23Cat: string;
  recordedPincode: string;
  recordedPincodeCat: string;
  censuscode2011: number;
  village: string;
  district: string;
  state: string;
  ur: string;
  initiatedCen: string;
  cgt1Cen: string;
  cgt2Cen: string;
  grtCen: string;
  activeCen: string;
  loanApps: number;
  cbFail: number;
  cbDone: number;
  cgt1: number;
  cgt2: number;
  grt: number;
  disbursed: number;
}

export interface Mapdata {
  id: number;
  latitude: number;
  longitude: number;
  createdAt: Date;
  updatedAt: Date;
  flag: string;
}
export interface Radardata {
  id: number;
  latitude: number;
  longitude: number;
  createdAt: Date;
  updatedAt: Date;
  flag: string;
}


export interface LatestSourcing {
  Pincode: number;
  latitude: number;
  longitude: number;
  createdAt: Date;
  updatedAt: Date;
  flag: string;
}

export interface MapTypeConfig {
  attribute: string;
  imageUrlCondition: (item: any) => string;
}


export interface Layer {
  name: string;
  visible: boolean;
  toggleVisibility(): void;
}



export interface LatestSourcing {
  censuscode2011: number;
  village: string;
  pincode: number;
  district: string;
  state: string;
  population: number;
  houseHolds: number;
  ur: string; // Assuming this is a string, adjust the type as necessary
  latMinBoundCentroid: number;
  longMinBoundCentroid: number;
  jun23Cat: string;
  visited: string;
}

export interface mixData {
  censuscode2011: number;
  village: string;
  pincode: string;
  district: string;
  population: number;
  houseHolds: number;
  ur: string; // Assuming U/R means Urban/Rural, so it's a string. Adjust if it's different.
  latMinBoundCentroid: number;
  longMinBoundCentroid: number;
  jun23Cat: string;
  centerCount: number;
  initiatedCen: number;
  cgt1Cen: number;
  cgt2Cen: number;
  grtCen: number;
  activeCen: number;
  loanApps: number;
  cbFail: number;
  cbDone: number;
  cgt1: number;
  cgt2: number;
  grt: number;
  disbursed: number;
  center: string;
  state: string;
  visited: string;
  branch_Distance:string;
  catStatus: string;
  key: string;
}


export interface User {
  id: number;
  deviceId: string;
  epochData: number;
  epochStored: number;
  latitude: number;
  longitude: number;
  delta_distance: number;
  delta_t : number;
  speed: number;
  mov_avg_spd: number;
  humanReadableDate : string;
  db_t:number;
  isActive?: boolean; 

}