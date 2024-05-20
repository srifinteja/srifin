import { Component, OnInit } from '@angular/core';
import { LayerVisibilityService } from '../color-layer-service';
@Component({
  selector: 'app-legend3',
  templateUrl: './legend3.component.html',
  styleUrls: ['./legend3.component.css']
})
export class Legend3Component implements OnInit {

  layerVisibility: {[key: string]: boolean} = {};

  constructor(private layerVisibilityService: LayerVisibilityService) {}

  ngOnInit(): void {
    this.layerVisibilityService.layerVisibility$.subscribe(visibility => {
      this.layerVisibility = visibility;
    });
  }

}
