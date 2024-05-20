import { ComponentFixture, TestBed } from '@angular/core/testing';

import { Legend3Component } from './legend3.component';

describe('Legend3Component', () => {
  let component: Legend3Component;
  let fixture: ComponentFixture<Legend3Component>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [Legend3Component]
    });
    fixture = TestBed.createComponent(Legend3Component);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
