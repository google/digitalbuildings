package www.google.com.digitalbuildings._0_0_1.fields;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.subfields.IWater;
import www.google.com.digitalbuildings._0_0_1.subfields.IFlowrate;
import www.google.com.digitalbuildings._0_0_1.subfields.ICondensing;
import www.google.com.digitalbuildings._0_0_1.subfields.ISensor;

public interface ICondensing_water_flowrate_sensor extends IField{

	public IRI iri();

    public void addComposedOfCondensing (ICondensing parameter);

	public Set<ICondensing> getComposedOfCondensing();

    public void addComposedOfFlowrate (IFlowrate parameter);

	public Set<IFlowrate> getComposedOfFlowrate();

    public void addComposedOfSensor (ISensor parameter);

	public Set<ISensor> getComposedOfSensor();

    public void addComposedOfWater (IWater parameter);

	public Set<IWater> getComposedOfWater();

}