package com.example.demo;

public class Mix {
    private int censuscode2011;
    private String village;
    private String pincode;
    private String district;
    private int population;
    private int houseHolds;
    private String ur; // Assuming U/R is a String. Adjust the data type as needed.
    private double latMinBoundCentroid;
    private double longMinBoundCentroid;
    private String jun23Cat;
    private int centerCount;
    private int initiatedCen;
    private int cgt1Cen;
    private int cgt2Cen;
    private int grtCen;
    private int activeCen;
    private int loanApps;
    private int cbFail;
    private int cbDone;
    private int cgt1;
    private int cgt2;
    private int grt;
    private int disbursed;
    private String center;
    private String state;
    private String visited;
    private String Branch_Distance;
    public int getCensuscode2011() {
        return censuscode2011;
    }

    public void setCensuscode2011(int censuscode2011) {
        this.censuscode2011 = censuscode2011;
    }

    public String getVillage() {
        return village;
    }

    public void setVillage(String village) {
        this.village = village;
    }

    public String getBranch_Distance() {
        return Branch_Distance;
    }

    public void setBranch_Distance(String branch_Distance) {
        Branch_Distance = branch_Distance;
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

    public int getPopulation() {
        return population;
    }

    public void setPopulation(int population) {
        this.population = population;
    }

    public int getHouseHolds() {
        return houseHolds;
    }

    public void setHouseHolds(int houseHolds) {
        this.houseHolds = houseHolds;
    }

    public String getUr() {
        return ur;
    }

    public void setUr(String ur) {
        this.ur = ur;
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

    public String getJun23Cat() {
        return jun23Cat;
    }

    public void setJun23Cat(String jun23Cat) {
        this.jun23Cat = jun23Cat;
    }

    public int getCenterCount() {
        return centerCount;
    }

    public void setCenterCount(int centerCount) {
        this.centerCount = centerCount;
    }

    public int getInitiatedCen() {
        return initiatedCen;
    }

    public void setInitiatedCen(int initiatedCen) {
        this.initiatedCen = initiatedCen;
    }

    public int getCgt1Cen() {
        return cgt1Cen;
    }

    public void setCgt1Cen(int cgt1Cen) {
        this.cgt1Cen = cgt1Cen;
    }

    public int getCgt2Cen() {
        return cgt2Cen;
    }

    public void setCgt2Cen(int cgt2Cen) {
        this.cgt2Cen = cgt2Cen;
    }

    public int getGrtCen() {
        return grtCen;
    }

    public void setGrtCen(int grtCen) {
        this.grtCen = grtCen;
    }

    public int getActiveCen() {
        return activeCen;
    }

    public void setActiveCen(int activeCen) {
        this.activeCen = activeCen;
    }

    public int getLoanApps() {
        return loanApps;
    }

    public void setLoanApps(int loanApps) {
        this.loanApps = loanApps;
    }

    public int getCbFail() {
        return cbFail;
    }

    public void setCbFail(int cbFail) {
        this.cbFail = cbFail;
    }

    public int getCbDone() {
        return cbDone;
    }

    public void setCbDone(int cbDone) {
        this.cbDone = cbDone;
    }

    public int getCgt1() {
        return cgt1;
    }

    public void setCgt1(int cgt1) {
        this.cgt1 = cgt1;
    }

    public int getCgt2() {
        return cgt2;
    }

    public void setCgt2(int cgt2) {
        this.cgt2 = cgt2;
    }

    public int getGrt() {
        return grt;
    }

    public void setGrt(int grt) {
        this.grt = grt;
    }

    public int getDisbursed() {
        return disbursed;
    }

    public void setDisbursed(int disbursed) {
        this.disbursed = disbursed;
    }

    public String getCenter() {
        return center;
    }

    public void setCenter(String center) {
        this.center = center;
    }

    public String getState() {
        return state;
    }

    public void setState(String state) {
        this.state = state;
    }

    @Override
    public String toString() {
        return "Mix{" +
                "censuscode2011=" + censuscode2011 +
                ", village='" + village + '\'' +
                ", pincode=" + pincode +
                ", district='" + district + '\'' +
                ", population=" + population +
                ", houseHolds=" + houseHolds +
                ", ur='" + ur + '\'' +
                ", latMinBoundCentroid=" + latMinBoundCentroid +
                ", longMinBoundCentroid=" + longMinBoundCentroid +
                ", jun23Cat='" + jun23Cat + '\'' +
                ", centerCount=" + centerCount +
                ", initiatedCen=" + initiatedCen +
                ", cgt1Cen=" + cgt1Cen +
                ", cgt2Cen=" + cgt2Cen +
                ", grtCen=" + grtCen +
                ", activeCen=" + activeCen +
                ", loanApps=" + loanApps +
                ", cbFail=" + cbFail +
                ", cbDone=" + cbDone +
                ", cgt1=" + cgt1 +
                ", cgt2=" + cgt2 +
                ", grt=" + grt +
                ", disbursed=" + disbursed +
                ", center='" + center + '\'' +
                ", state='" + state + '\'' +
                ", visited='" + visited + '\'' +
                ", catStatus='" + catStatus + '\'' +
                ", key='" + key + '\'' +
                '}';
    }

    public String getVisited() {
        return visited;
    }

    public void setVisited(String visited) {
        this.visited = visited;
    }

    public String getCatStatus() {
        return catStatus;
    }

    public void setCatStatus(String catStatus) {
        this.catStatus = catStatus;
    }

    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }

    private String catStatus;
    private String key;
}
