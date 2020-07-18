package www.google.com.digitalbuildings._0_0_1.fields;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.subfields.IFlowrate;
import www.google.com.digitalbuildings._0_0_1.subfields.IAir;
import www.google.com.digitalbuildings._0_0_1.subfields.IDischarge;
import www.google.com.digitalbuildings._0_0_1.subfields.ISensor;

public interface IDischarge_air_flowrate_sensor extends IField{

	public IRI iri();

    public void addComposedOfAir (IAir parameter);

	public Set<IAir> getComposedOfAir();

    public void addComposedOfDischarge (IDischarge parameter);

	public Set<IDischarge> getComposedOfDischarge();

    public void addComposedOfFlowrate (IFlowrate parameter);

	public Set<IFlowrate> getComposedOfFlowrate();

    public void addComposedOfSensor (ISensor parameter);

	public Set<ISensor> getComposedOfSensor();

}