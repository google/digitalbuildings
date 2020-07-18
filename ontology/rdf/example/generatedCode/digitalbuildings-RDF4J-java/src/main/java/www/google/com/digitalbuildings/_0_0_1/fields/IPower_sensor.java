package www.google.com.digitalbuildings._0_0_1.fields;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.subfields.IPower;
import www.google.com.digitalbuildings._0_0_1.subfields.ISensor;

public interface IPower_sensor extends IField{

	public IRI iri();

    public void addComposedOfPower (IPower parameter);

	public Set<IPower> getComposedOfPower();

    public void addComposedOfSensor (ISensor parameter);

	public Set<ISensor> getComposedOfSensor();

}