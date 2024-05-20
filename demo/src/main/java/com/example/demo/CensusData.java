package com.example.demo;
public class CensusData {
    //source_map
    private String censusCode2011;
    private String village;
    private String pincode;
    private String district;

    public String getCensusCode2011() {
        return censusCode2011;
    }

    public void setCensusCode2011(String censusCode2011) {
        this.censusCode2011 = censusCode2011;
    }

    public String getVisited() {
        return visited;
    }

    public String getVillage() {
        return village;
    }

    public void setVillage(String village) {
        this.village = village;
    }

    public String getPincode() {
        return pincode;
    }

    public void setPincode(String pincode) {
        this.pincode = pincode;
    }

    public String getDistrict() {
        return district;
    }

    public void setDistrict(String district) {
        this.district = district;
    }

    public String getState() {
        return state;
    }

    public void setState(String state) {
        this.state = state;
    }

    public long getTotP2011() {
        return totP2011;
    }

    public void setTotP2011(long totP2011) {
        this.totP2011 = totP2011;
    }

    public long getNoHh2011() {
        return noHh2011;
    }

    public void setNoHh2011(long noHh2011) {
        this.noHh2011 = noHh2011;
    }

    public String getTru2011() {
        return tru2011;
    }

    public void setTru2011(String tru2011) {
        this.tru2011 = tru2011;
    }

    public double getLatMinBoundCentroid() {
        return latMinBoundCentroid;
    }

    public void setLatMinBoundCentroid(double latMinBoundCentroid) {
        this.latMinBoundCentroid = latMinBoundCentroid;
    }

    public double getLongMinBoundCentroid() {
        return longMinBoundCentroid;
    }

    public void setLongMinBoundCentroid(double longMinBoundCentroid) {
        this.longMinBoundCentroid = longMinBoundCentroid;
    }

    public String getFinalCat() {
        return finalCat;
    }

    public void setFinalCat(String finalCat) {
        this.finalCat = finalCat;
    }

    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }

    public String getDeepStatus() {
        return deepStatus;
    }

    public void setDeepStatus(String deepStatus) {
        this.deepStatus = deepStatus;
    }

    public double getbDist() {
        return bDist;
    }

    public void setbDist(double bDist) {
        this.bDist = bDist;
    }

    public String isVisited() {
        return visited;
    }

    public void setVisited(String visited) {
        this.visited = visited;
    }

    private String state;
    private long totP2011;
    private long noHh2011;
    private String tru2011;
    private double latMinBoundCentroid;
    private double longMinBoundCentroid;
    private String finalCat;
    private String status;
    private String deepStatus;
    private double bDist;
    private String visited;

    @Override
    public String toString() {
        return "CensusData{" +
                "censusCode2011='" + censusCode2011 + '\'' +
                ", village='" + village + '\'' +
                ", pincode='" + pincode + '\'' +
                ", district='" + district + '\'' +
                ", state='" + state + '\'' +
                ", totP2011=" + totP2011 +
                ", noHh2011=" + noHh2011 +
                ", tru2011='" + tru2011 + '\'' +
                ", latMinBoundCentroid=" + latMinBoundCentroid +
                ", longMinBoundCentroid=" + longMinBoundCentroid +
                ", finalCat='" + finalCat + '\'' +
                ", status='" + status + '\'' +
                ", deepStatus='" + deepStatus + '\'' +
                ", bDist=" + bDist +
                ", visited='" + visited + '\'' +
                '}';
    }
}
