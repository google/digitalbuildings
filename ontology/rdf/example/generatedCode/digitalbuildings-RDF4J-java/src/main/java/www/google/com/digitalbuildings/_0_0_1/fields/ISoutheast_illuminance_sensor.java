package www.google.com.digitalbuildings._0_0_1.fields;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.subfields.ISoutheast;
import www.google.com.digitalbuildings._0_0_1.subfields.IIlluminance;
import www.google.com.digitalbuildings._0_0_1.subfields.ISensor;

public interface ISoutheast_illuminance_sensor extends IField{

	public IRI iri();

    public void addComposedOfIlluminance (IIlluminance parameter);

	public Set<IIlluminance> getComposedOfIlluminance();

    public void addComposedOfSensor (ISensor parameter);

	public Set<ISensor> getComposedOfSensor();

    public void addComposedOfSoutheast (ISoutheast parameter);

	public Set<ISoutheast> getComposedOfSoutheast();

}