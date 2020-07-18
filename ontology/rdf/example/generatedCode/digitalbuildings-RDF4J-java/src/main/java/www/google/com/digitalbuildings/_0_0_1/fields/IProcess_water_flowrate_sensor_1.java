package www.google.com.digitalbuildings._0_0_1.fields;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.subfields.IWater;
import www.google.com.digitalbuildings._0_0_1.subfields.IFlowrate;
import www.google.com.digitalbuildings._0_0_1.subfields.IProcess;
import www.google.com.digitalbuildings._0_0_1.subfields.ISensor;

public interface IProcess_water_flowrate_sensor_1 extends IField{

	public IRI iri();

    public void addComposedOfFlowrate (IFlowrate parameter);

	public Set<IFlowrate> getComposedOfFlowrate();

    public void addComposedOfProcess (IProcess parameter);

	public Set<IProcess> getComposedOfProcess();

    public void addComposedOfSensor (ISensor parameter);

	public Set<ISensor> getComposedOfSensor();

    public void addComposedOfWater (IWater parameter);

	public Set<IWater> getComposedOfWater();

}