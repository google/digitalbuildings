package www.google.com.digitalbuildings._0_0_1.fields;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.subfields.IWest;
import www.google.com.digitalbuildings._0_0_1.subfields.IIlluminance;
import www.google.com.digitalbuildings._0_0_1.subfields.ISensor;

public interface IWest_illuminance_sensor extends IField{

	public IRI iri();

    public void addComposedOfIlluminance (IIlluminance parameter);

	public Set<IIlluminance> getComposedOfIlluminance();

    public void addComposedOfSensor (ISensor parameter);

	public Set<ISensor> getComposedOfSensor();

    public void addComposedOfWest (IWest parameter);

	public Set<IWest> getComposedOfWest();

}