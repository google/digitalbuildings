package www.google.com.digitalbuildings._0_0_1.fields;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.subfields.IEast;
import www.google.com.digitalbuildings._0_0_1.subfields.IIlluminance;
import www.google.com.digitalbuildings._0_0_1.subfields.ISensor;

public interface IEast_illuminance_sensor extends IField{

	public IRI iri();

    public void addComposedOfEast (IEast parameter);

	public Set<IEast> getComposedOfEast();

    public void addComposedOfIlluminance (IIlluminance parameter);

	public Set<IIlluminance> getComposedOfIlluminance();

    public void addComposedOfSensor (ISensor parameter);

	public Set<ISensor> getComposedOfSensor();

}