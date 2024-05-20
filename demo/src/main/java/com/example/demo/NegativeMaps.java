package com.example.demo;

public class NegativeMaps {
    private String branch;
    private String latestApplication;
    private String pincode;
    private String jun23Cat;
    private String recordedPincode;
    private String recordedPincodeCat;
    private Long censuscode2011;

    public String getBranch() {
        return branch;
    }

    public void setBranch(String branch) {
        this.branch = branch;
    }

    public String getLatestApplication() {
        return latestApplication;
    }

    public void setLatestApplication(String latestApplication) {
        this.latestApplication = latestApplication;
    }

    public String getPincode() {
        return pincode;
    }

    public void setPincode(String pincode) {
        this.pincode = pincode;
    }

    public String getJun23Cat() {
        return jun23Cat;
    }

    public void setJun23Cat(String jun23Cat) {
        this.jun23Cat = jun23Cat;
    }

    public String getRecordedPincode() {
        return recordedPincode;
    }

    public void setRecordedPincode(String recordedPincode) {
        this.recordedPincode = recordedPincode;
    }

    public String getRecordedPincodeCat() {
        return recordedPincodeCat;
    }

    public void setRecordedPincodeCat(String recordedPincodeCat) {
        this.recordedPincodeCat = recordedPincodeCat;
    }

    public Long getCensuscode2011() {
        return censuscode2011;
    }

    public void setCensuscode2011(Long censuscode2011) {
        this.censuscode2011 = censuscode2011;
    }

    public String getVillage() {
        return village;
    }

    public void setVillage(String village) {
        this.village = village;
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

    public String getUr() {
        return ur;
    }

    public void setUr(String ur) {
        this.ur = ur;
    }

    public String getInitiatedCen() {
        return initiatedCen;
    }

    public void setInitiatedCen(String initiatedCen) {
        this.initiatedCen = initiatedCen;
    }

    public String getCgt1Cen() {
        return cgt1Cen;
    }

    public void setCgt1Cen(String cgt1Cen) {
        this.cgt1Cen = cgt1Cen;
    }

    public String getCgt2Cen() {
        return cgt2Cen;
    }

    public void setCgt2Cen(String cgt2Cen) {
        this.cgt2Cen = cgt2Cen;
    }

    public String getGrtCen() {
        return grtCen;
    }

    public void setGrtCen(String grtCen) {
        this.grtCen = grtCen;
    }

    public String getActiveCen() {
        return activeCen;
    }

    public void setActiveCen(String activeCen) {
        this.activeCen = activeCen;
    }

    public Integer getLoanApps() {
        return loanApps;
    }

    public void setLoanApps(Integer loanApps) {
        this.loanApps = loanApps;
    }

    public Integer getCbFail() {
        return cbFail;
    }

    @Override
    public String toString() {
        return "NegativeMaps{" +
                "branch='" + branch + '\'' +
                ", latestApplication='" + latestApplication + '\'' +
                ", pincode='" + pincode + '\'' +
                ", jun23Cat='" + jun23Cat + '\'' +
                ", recordedPincode='" + recordedPincode + '\'' +
                ", recordedPincodeCat='" + recordedPincodeCat + '\'' +
                ", censuscode2011=" + censuscode2011 +
                ", village='" + village + '\'' +
                ", district='" + district + '\'' +
                ", state='" + state + '\'' +
                ", ur='" + ur + '\'' +
                ", initiatedCen='" + initiatedCen + '\'' +
                ", cgt1Cen='" + cgt1Cen + '\'' +
                ", cgt2Cen='" + cgt2Cen + '\'' +
                ", grtCen='" + grtCen + '\'' +
                ", activeCen='" + activeCen + '\'' +
                ", loanApps=" + loanApps +
                ", cbFail=" + cbFail +
                ", cbDone=" + cbDone +
                ", cgt1=" + cgt1 +
                ", cgt2=" + cgt2 +
                ", grt=" + grt +
                ", disbursed=" + disbursed +
                '}';
    }

    public void setCbFail(Integer cbFail) {
        this.cbFail = cbFail;
    }

    public Integer getCbDone() {
        return cbDone;
    }

    public void setCbDone(Integer cbDone) {
        this.cbDone = cbDone;
    }

    public Integer getCgt1() {
        return cgt1;
    }

    public void setCgt1(Integer cgt1) {
        this.cgt1 = cgt1;
    }

    public Integer getCgt2() {
        return cgt2;
    }

    public void setCgt2(Integer cgt2) {
        this.cgt2 = cgt2;
    }

    public Integer getGrt() {
        return grt;
    }

    public void setGrt(Integer grt) {
        this.grt = grt;
    }

    public Integer getDisbursed() {
        return disbursed;
    }

    public void setDisbursed(Integer disbursed) {
        this.disbursed = disbursed;
    }

    private String village;
    private String district;
    private String state;
    private String ur;
    private String initiatedCen;
    private String cgt1Cen;
    private String cgt2Cen;
    private String grtCen;
    private String activeCen;
    private Integer loanApps;
    private Integer cbFail;
    private Integer cbDone;
    private Integer cgt1;
    private Integer cgt2;
    private Integer grt;
    private Integer disbursed;

    // Constructor, optionally if needed
    public NegativeMaps() {
    }

}
